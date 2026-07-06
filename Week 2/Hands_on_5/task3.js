// Task 3: Aggregation Pipeline

//71. Calculate average rating and feedback count for 2022-ODD

db.feedback.aggregate([
{
    $match: { semester: "2022-ODD" }
},
{
    $group: {
        _id: "$course_code",
        feedback_count: { $sum: 1 },
        average_rating: { $avg: "$rating" }
    }
},
{
    $sort: { feedback_count: -1 }
}
]);


//72. Display rounded average rating

db.feedback.aggregate([
{
    $match: { semester: "2022-ODD" }
},
{
    $group: {
        _id: "$course_code",
        average_rating: { $avg: "$rating" },
        feedback_count: { $sum: 1 }
    }
},
{
    $project: {
        _id: 0,
        course_code: "$_id",
        average_rating: { $round: ["$average_rating", 1] },
        feedback_count: 1
    }
},
{
    $sort: { average_rating: -1 }
}
]);


//73. Count occurrences of each tag

db.feedback.aggregate([
{
    $unwind: "$tags"
},
{
    $group: {
        _id: "$tags",
        total: { $sum: 1 }
    }
},
{
    $sort: { total: -1 }
}
]);


//74. Create an index on course_code

db.feedback.createIndex({
    course_code: 1
});


// Verify index

db.feedback.find({
    course_code: "CS101"
}).explain("executionStats");


// Expected Output:
//
// Aggregation 1:
// Displays one record for each course with
// average rating and total feedback.
//
// Aggregation 2:
// Shows average_rating rounded to one decimal.
//
// Aggregation 3:
// Lists tags in descending order of frequency.
//
// Explain:
// Execution plan should use "IXSCAN"
// instead of "COLLSCAN". \