// Task 2: CRUD Operations

//65. Display all feedback with maximum rating

db.feedback.find({
    rating: 5
});


//66. Find feedback for CS101 containing the "interactive" tag

db.feedback.find({
    course_code: "CS101",
    tags: "interactive"
});


//67. Show only selected fields

db.feedback.find(
    {},
    {
        _id: 0,
        student_id: 1,
        course_code: 1,
        rating: 1
    }
);


//68. Mark low-rated feedback

db.feedback.updateMany(
    {
        rating: { $lte: 2 }
    },
    {
        $set: { needs_review: true }
    }
);


// Verify

db.feedback.find({
    needs_review: true
});


//69. Add a new tag for reviewed feedback

db.feedback.updateMany(
    {
        needs_review: true
    },
    {
        $push: { tags: "checked" }
    }
);


// Verify

db.feedback.find({
    needs_review: true
});


//70. Remove feedback from the 2021-EVEN semester

db.feedback.deleteMany({
    semester: "2021-EVEN"
});


// Verify

db.feedback.find();

db.feedback.countDocuments();

// Expected Output:
// 5 documents remaining