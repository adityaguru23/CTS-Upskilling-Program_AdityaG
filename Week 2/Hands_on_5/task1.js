// Task 1: Create Collection and Insert Documents

//60. Create database

use("college_feedback_db");


//61. Create feedback collection

db.createCollection("feedback");


//62. Insert feedback documents

db.feedback.insertMany([
{
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent course with clear explanations.",
    tags: ["interactive","well-structured"],
    submitted_at: new Date("2022-11-30T10:00:00Z"),
    attachments: [{ filename: "notes.pdf", size_kb: 220 }]
},
{
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Good practical sessions.",
    tags: ["interactive","helpful"],
    submitted_at: new Date("2022-11-28T09:30:00Z"),
    attachments: [{ filename: "assignment.pdf", size_kb: 180 }]
},
{
    student_id: 3,
    course_code: "CS102",
    semester: "2022-EVEN",
    rating: 3,
    comments: "Average but informative.",
    tags: ["informative"],
    submitted_at: new Date("2022-12-02T11:15:00Z"),
    attachments: [{ filename: "lab.pdf", size_kb: 210 }]
},
{
    student_id: 4,
    course_code: "EC101",
    semester: "2021-EVEN",
    rating: 2,
    comments: "Needs more examples.",
    tags: ["difficult"],
    submitted_at: new Date("2021-11-20T08:45:00Z"),
    attachments: [{ filename: "review.pdf", size_kb: 120 }]
},
{
    student_id: 5,
    course_code: "ME101",
    semester: "2023-ODD",
    rating: 5,
    comments: "Excellent learning experience.",
    tags: ["practical","interesting"],
    submitted_at: new Date("2023-10-10T12:30:00Z"),
    attachments: [{ filename: "summary.pdf", size_kb: 200 }]
},
{
    student_id: 6,
    course_code: "CS103",
    semester: "2023-ODD",
    rating: 4,
    comments: "Good coding assignments.",
    tags: ["coding","challenging"],
    submitted_at: new Date("2023-10-12T14:00:00Z")
}
]);


//63. Display one document without attachments

db.feedback.find({ student_id: 6 });


//64. Count the number of documents

db.feedback.countDocuments();

// Expected Output:
// 6