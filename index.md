---
layout: default
title: Course syllabus
description: Policies, assessment, learning outcomes, and course guidance for CPEN 221 A/B.
term: Fall 2026
permalink: /
---

# Instructional Team

### Instructors

- Prof. Karthik Pattabiraman
- Prof. Simon Oya

### Teaching Assistants

- Rudransh Kumar, MASc student, Electrical and Computer Engineering [Head TA]
- Amirreza Soleimanbeigi, MASc student, Electrical and Computer Engineering
- Rhys Byers, BASc student, Computer Engineering
- Ali Osman, BASc student, Computer Engineering
- Dana Ebadi, BASc student, Computer Engineering
- Lucas Beitel, BASc student, Computer Engineering
- Geoffrey Bian, BASc student, Computer Engineering
- Donghwa Kim, BASc student, Computer Engineering

# Class Meeting Times

The class has scheduled lecture sessions, tutorial sessions and lab sessions.

**Lectures:** We will meet for lecture sessions on Tuesdays and Thursdays (11am to 12:20pm) in [CHEM B150](https://learningspaces.ubc.ca/find-a-space/?classroom=chem-b150&building=&filters=%257B%257D). 
We will use these sessions to reinforce concepts that you should have done some pre-reading about, and these sessions will involve some interactivity and coding demonstrations.

**Tutorials:** Tutorial sessions will be held on Mondays at 2pm in [ESB 1013](https://learningspaces.ubc.ca/classrooms/esb-1013/). 
These sessions focus on exploring and understanding the foundational principles taught in lectures using relevant examples and problems and are often closely tied with the labs. 
They are also an opportunity for learning how to use important parts of the programming toolkit like the IDE, build tools, and debugger.

**Labs:** You should have all signed up for a lab section, which will normally meet once a week (excluding the first week of classes). 
Teaching assistants will lead these sessions, often providing an overview of some concept or task and being available to answer questions. The different lab sections are:

| **Time**             | **Location** | **Section**   |
| -------------------- | ------------ | ------------- |
| Mondays 4-5:30pm     | MCLD 4006    | CPEN 221B L1C |
| Wednesdays 8:30-10am | MCLD 4002    | CPEN 221A L1B |
| Wednesdays 8:30-10am | MCLD 4006    | CPEN 221A L1A |
| Wednesdays 3-4:30pm  | MCLD 4002    | CPEN 221A L1D |
| Wednesdays 3-4:30pm  | MCLD 4006    | CPEN 221B L1B |
| Thursdays 1:30-3pm   | MCLD 4002    | CPEN 221A L1C |
| Fridays 2-3:30pm     | MCLD 4006    | CPEN 221B L1A |


# Core Topics

The course topics are organized into four modules. 
We will cover all of the topics mostly in keeping with the module structure outlined below, but there will be some key departures in sequencing when it is important to understand some concepts earlier (e.g., aspects of memory management in Module 3) even though they may be listed in a later module.

### Module 1: Static Typing, Specifications, Exceptions, Testing

- Static checking and types
- Useful data abstractions (lists, sets, maps)
- Procedural specifications
    - Why specifications?
    - The structure of procedural specifications
    - Strength of specifications
- Testing
    - Selecting test cases
    - Testing and specifications
- Exceptions

### Module 2: Abstract Data Types

- Mutability and immutability
- Abstract data types
- Robust types
    - Representation invariants and abstraction functions
- Subtypes
    - The Liskov Substitution Principle

### Module 3: Recursion and More

- Recursion
- Recursive Types
- Concise idioms: streams and map-filter-reduce operations
- How computers work
    - A model of computer systems
    - How programs are executed and memory is managed
- (Optional) Grammars
- Regular expressions

### Module 4: Concurrent Programming

- Concurrency vs. parallelism
- Multi-threading
- Message passing and network programming
- Fork-join parallelism
- Shared memory programming
- Concurrent programs and safety

# Learning Outcomes

### Module 1

- **Static checking and types**
    - Explain the difference between static and dynamic checking
    - Explain the value of static type checking
- **Useful data abstractions (lists, sets, maps)**
    - Describe the operations on three common data abstractions: lists, sets, and maps
    - Use lists, sets and maps to solve computational problems
- **Procedural specifications**
    - Explain the need for specifications
    - Describe the structure of specifications
    - Write procedural specifications for a given implementation
    - Write procedural specifications given partial requirements
    - Identify ambiguities in a given specification
    - Determine is a specification is underspecified or not
    - Compare specifications based on their strength
- **Testing**
    - Explain why we rely on testing
    - Identify unit tests based on input-space partitioning
    - Write test cases based on a given specification
    - Write test cases using a standard framework (like JUnit)
    - Describe the differences between blackbox and whitebox testing
    - Explain the role of test coverage in software quality
    - Write test cases to achieve code coverage
    - Measure code coverage achieved through tests
- **Exceptions**
    - Explain the need for exceptions
    - Use exceptions in programs
    - Identify the strengths and weaknesses of exceptions in modern programming languages

## Module 2

- **Mutability and immutability**
    - Explain mutability and immutability in the context of data types
    - Explain the value of immutability of data types
    - Explain the value of mutability of data types
    - Identify the threats to mutability of a data type
    - Implement data types that are immutable
- **Abstract data types**
    - Define a data type
    - Classify the types of operations on a data type
    - Explain representation invariants and abstraction functions, and their role in reasoning about data types
    - Choose suitable representations for a data type
    - Write representation invariants and abstraction functions for a data type implementation
    - Explain what an interface is and how it relates to data types
    - Implement types that conform to an interface
    - Define equality and the types of object equality
    - Implement appropriate notions of equality for immutable and mutable types
- **Subtypes**
    - Explain subtyping
    - Distinguish between subtyping and subclassing in languages such as Java
    - Explain the role of specification strength when reasoning about subtypes
    - Explain the Liskov Substitution Principle
    - Implement subtypes
    - Explain inheritance and polymorphism
    - Make design choices about when to use inheritance and when not to
    - Use interfaces and composition to achieve safer code reuse

## Module 3

- **Recursion**
    - Explain recursion as a mathematical idea
    - Explain recursion as implemented in a computer system
    - Use recursive methods to solve problems
    - Use induction to reason about the correctness of recursive solutions
    - Explain the advantages of recursion in establishing code correctness
    - Explain the performance implications of recursion
    - Transform recursive implementations to iterative implementations
- **Recursive Types**
    - Implement data types using recursive structure
    - Explain the recursive implementation of a data type such as a list
    - Explain — using recursion — structures such as trees, binary trees, and binary search trees
    - Implement binary trees
- **Concise idioms: streams and map-filter-reduce operations**
    - Describe the basic operations in stream processing
    - Describe the role of stream processing in expressing intent in a program
    - Use stream processing to solve programming problems
    - Describe higher-order functions and their role in stream processing
- **How computers work**
    - Describe the von Neumann model of computing
    - Explain the basics of how a computer works
    - Explain the role of a function-call stack in program execution
    - Explain the role of the memory heap in a computer system
    - Explain a buffer overflow attack

## Module 4

- **Concurrency vs. parallelism**
    - Distinguish between parallelism and concurrency
    - Explain the need for concurrent programming
    - Multi-threading
    - Define processes and threads
    - Write programs using multiple threads
- **Message passing and network programming**
    - Describe the message passing model of programming
    - Explain client-server programming
    - Implement the client-server pattern using network sockets
- **Fork-join parallelism**
    - Explain the fork-join approach to parallel programming
    - Implement simple parallel programs using a standard fork-join framework
- **Shared memory programming**
    - Explain shared memory programming
    - Describe the challenges of shared memory programming such as data races and bad interleavings
    - Implement concurrent programs that share memory
    - Use mechanisms such as synchronization and locking to avoid data races and bad interleavings
- **Concurrent programs and safety**
    - Write thread-safety arguments to establish that a concurrent program does not have a data race or bad interleavings

## Software in Practice

- Use of modern IDEs and version control (git)
- Demonstrate implementation of moderate sized software (100s - 1000s of lines of code)
- Develop algorithms for tasks with simple to moderate complexity
- Demonstrate some ability in implementing software with greater algorithmic sophistication

# Policies

# Code of Conduct

### Introduction

- Diversity and inclusion make our community strong.
- We encourage participation from the most varied and diverse backgrounds possible and want to be very clear about where we stand.
- Our goal is to maintain a safe, helpful and friendly community for everyone, regardless of experience, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, nationality, or other defining characteristics.
- This code and related procedures also apply to unacceptable behaviour occurring outside the scope of community activities, in all community venues— online and in-person— as well as in all one-on-one communications, and anywhere such behaviour has the potential to adversely affect the safety and well-being of community members.
- Unprofessional conduct that violates safety policies or posted laboratory rules can result in significant penalties that include loss of access to departmental facilities and/or a reduction in grades. (Also see: [ECE Safety Guidelines and Policies](http://ece.ubc.ca/safety).)
- “The best possible environment for working, learning and living is one in which respect, civility, diversity, opportunity and inclusion are valued. Everyone at the University of British Columbia is expected to conduct themselves in a manner that upholds these principles in all communications and interactions with fellow UBC community members and the public in all University-related settings.” —(Extracted from the [UBC Respectful Environment Statement](http://www.hr.ubc.ca/respectful-environment/).)

### Expected Behaviour

- Be welcoming.
- Be kind.
- Look out for each other.

### Unacceptable Behaviour

- Conduct or speech which might be considered sexist, racist, homophobic, transphobic, ableist or otherwise discriminatory or offensive in nature.
- Do not use unwelcome, suggestive, derogatory or inappropriate nicknames or terms.
- Do not show disrespect towards others. (Jokes, innuendo, dismissive attitudes.)
- Intimidation or harassment (online or in-person). Please read the [Django Code of Conduct](https://www.djangoproject.com/conduct/) for how we interpret harassment.
- Disrespect towards differences of opinion.
- Inappropriate attention or contact. Be aware of how your actions affect others. If it makes someone uncomfortable, stop.
- Not understanding the differences between constructive criticism and disparagement.
- Sustained disruptions.
- Violence, threats of violence or violent language.
- Sharing messages outside of the course’s discussion forum without permission of the poster.

### Enforcement

- Understand that speech and actions have consequences, and unacceptable behaviour will not be tolerated.
- If you are the subject of or witness to any violations of this Code of Conduct, please contact us by writing to the admin team [instructors]. This group of people will be the final decision-makers and enforcers on the Code of Conduct violations.
- If violations occur, organizers will take any action they deem appropriate for the infraction, up to and including expulsion.

# Academic Integrity

You should familiarize yourself with UBC’s [policy on student conduct and discipline](http://www.calendar.ubc.ca/vancouver/index.cfm?tree=3,54,0,0). The penalties for cheating are serious: you can fail a class, receive a letter of reprimand that will also appear on your university record, be suspended or be expelled.

Everything you submit as work in this course must be your own, or work completed as permitted within a team.

If you are feeling stressed, come talk to the instructor or the TAs to get help – at the labs, or the posted office hours, or make an appointment. Do not be afraid to come in and say you’re confused, we are here to help you get “unconfused.” Of course, it is good to come talk to us before you are completely overwhelmed.

You should also read [Tamara Munzner](http://www.cs.ubc.ca/~tmm/)'s writeup on [Cheating: The List of Things I Never Want To Hear Again](http://www.cs.ubc.ca/~tmm/courses/cheat.html).

Your Solutions: You must individually compose all of your solutions. The term solutions refers to any of the products created when completing a programming assignment (or other assigned tasks), such as source code (including comments) and other documents. It includes both finished and unfinished products, regardless of correctness or completeness.

- You must never give or expose your solutions to a programming assignment (or variant of an assignment) to anyone who is taking CPEN 221 now or who might take CPEN 221 in the future. For example, you may not place your solutions in a public location (such as a website, a public code repository, or a printout left in a lab). If you leave your computer unattended, be sure to protect it with a password.
- You must never receive or view someone else’s solutions to a programming assignment (or variant of an assignment).

These rules continue to apply even after the semester is over.

# Assessment and Grading

### Activities

Your understanding of the course material will be assessed using a variety of course activities. 
The primary activities that we will use are indicated below. The total number of points you can obtain are described as follows.

(total # of points for an activity) = (# of assignments for the activity) x (max # of points attainable for any assignments of the activity) x (weight associated with the activity)

- **[300 pts] Mini-Projects (MPs)**: The course will involve three mini-projects that will need to be completed individually. The mini-projects are opportunities to synthesize most of the course material and demonstrate one’s ability to implement correct, comprehensible and changeable software. Mini-Projects will span several weeks, allowing sufficient time for learning and implementation. Each mini-project will be graded on a scale of 0-10 and they have a weight of 10 when determining the final grade. (Total number of points: 3 x 10 x 10 = 300.)
- **[162 pts] Labs**: Each week, there will be shorter activities that will touch upon recent topics, and will typically involve an overview or discussion led by the teaching assistants during the lab sessions. The labs may include weekly programming tasks for additional practice. You may collaborate with one other student on these activities. Lab work should, however, be submitted individually. You must indicate who you collaborated with for each lab activity. There are a total of 10 lab activities, each graded on a scale of 0-9, and they will have a weight of 2 when determining the final grade. We will use the best 9 lab grades in the final grade computation. (Total number of points: 9 x 9 x 2 = 162.)
- **[550 pts] Quizzes and Final Exam**: To demonstrate an understanding of the principles of software construction, you will be examined periodically over the term. The course content is organized into four modules, but assessed in five parts, so that each part covers a smaller amount of material. The first four parts will be assessed during the term, and the fifth part will be assessed in the final exam. The final exam will also contain additional sections covering content from the previous four parts. We will take the better performance across the in-term quiz and final exam section to determine the grade for each of the four parts, whereas the fifth part is examined only in the final exam. Each quiz grade will have a weight of 11 in the final grade computation. The quizzes/exam will be scheduled in the computer-based testing facility (ORCA) and you will be able to select a time slot within a range of days to attempt the quiz or final exam. (Total number of points: 5 x 10 x 11 = 550.)
- **[250 pts] Project (CPEN 221A only)**: If you are registered for CPEN 221A then you must complete a group project in addition to other assessments. The project is 25 points and has a weight of 10. (Total number of points: 1 x 25 x 10 = 250.)

At the end of the term, we will aggregate your performance across all activities, as a weighted sum, to determine a final grade. 
Your final grade will be computed using the following thresholds for different letter grades and we will apply a linear interpolation to assign a numeric score between the bounds for the associated letter grade. The thresholds are different for students in CPEN 221A and CPEN 221B because of the additional project in CPEN 221A.

Example: Using the table below, a student in CPEN 221A who obtains 1060 points will have a final grade of 81, computed as (1060-1047)/(1098-1047) x (84-80) + 80 and rounded suitably.

| **Letter Grade** | **Grade Threshold** |           | **Numeric Score** |     |
| ---------------- | ------------------- | --------- | ----------------- | --- |
|                  | CPEN 221A           | CPEN 221B | Min               | Max |
| Max              | 1262                | 1012      |                   |     |
| A+               | 1224                | 982       | 90                | 100 |
| A.               | 1098                | 880       | 85                | 89  |
| A-               | 1047                | 840       | 80                | 84  |
| B+               | 997                 | 799       | 76                | 79  |
| B.               | 883                 | 708       | 72                | 75  |
| B-               | 833                 | 668       | 68                | 71  |
| C+               | 782                 | 627       | 65                | 67  |
| C.               | 694                 | 557       | 60                | 64  |
| C-               | 581                 | 466       | 55                | 59  |
| F.               | <= 580              | <= 465    | 0                 | 45  |

### **Bonus Points from Piazza Contributions**

We will provide some credit for being active in Piazza and helping answering questions from other students.

- 5 bonus points for the top answerer
- 4 bonus points for top 2.5% answerers
- 3 bonus points for top 5% answerers

### **Regrading Requests**

Regrading requests should be submitted to the course staff per the regrade policy for the assignment to the entire teaching team within one week of grade release. Instructions for how to make regrade requests will be made available via Piazza. The course staff will get back to the submitted requests within two weeks of the request and the decision is final.

**Exam Schedule**

> **Fall 2026 exam schedule:** Dates and locations will be posted here after they are confirmed.

# Use of Generative AI

In line with [UBC's Guidelines for all uses of GenAI in Teaching & Learning](https://genai.ubc.ca/guidance/teaching-learning-guidelines/guidelines-for-all-uses-of-genai-in-teaching-learning/), here we explicitly describe this course's policy on generative AI. According to UBC guidelines, *"Student use of GenAI outside of these stated rules may be considered academic misconduct."* 
In CPEN 221, the use of generative AI is completely banned for some assessments and conditionally permitted for others. Whenever generative AI is permitted for an assessment, you are required to abide by the assessment's generative AI use policy. These policies, *which may vary across assessments*, can include: 

1. Constraints on how generative AI might be used;
2. Disclosure & reporting requirements to document your use; and
3. A mandatory written reflection. 

If you use generative AI, where permitted, you are still fully responsible for all work submitted (same as in any real-world work environment). If you do not use generative AI where permitted, you are still responsible for declaring “no use” in a manner prescribed by the assessment's generative AI policy. 

We consider instances where two or more students submit identical or very similar code to be academic misconduct, irrespective of how the students might have arrived at similar submissions. We have reviewed 1000s of pairs of submissions each year, and the likelihood of two independent efforts being very similar is astonishingly low.  So, it is your responsibility to understand the rules surrounding the use of generative AI *for each assessment* carefully to maintain the academic integrity of your submissions, seek clarifications where required before submitting your work, and follow the rules carefully.

The following table summarizes the assessments for which generative AI tools are either completely banned or conditionally permitted in accordance with the assessment's generative AI policy.

| **Assessment**                         | **Use of Generative AI Tools** |
| -------------------------------------- | ------------------------------ |
| *Mini-Projects (MPs)*                  | Conditionally permitted        |
| *Labs*                                 | Completely banned              |
| *Quizzes & Final Exam*                 | Completely banned              |
| *CPEN221A Project*                     | Conditionally permitted        |

# Late Submissions and Missed Exams

## Late submissions

For individual work (labs and mini-projects), we will offer some slack to account for different possibilities.

- This form [TO BE ADDED!] can be used to indicate your use of late days. It is your responsibility to communicate the use of late days to the course staff through the administered poll, by latest 24 hours after your submission. Otherwise, the late days will not be accounted, and your latest code commit by the original deadline will be considered.
- **IMPORTANT**: if you use a late day, you cannot take it back! Make sure you only fill the late day form when you actually need the late day.
- You can submit up to 5 labs one day (24 hours) late with no penalty. 
- We will allow you 3 late days that you can choose to distribute in increments of one day across the three mini-projects. (You can use one late day per mini-project, or all three for one mini-project, or one extra day for one mini-project and two extra days for a second mini-project.)
- Any other concession will be on a case-by-case basis and will require a clear and acceptable rationale. (We will provide such concessions only in extenuating circumstances. For instance, we only use the best 9 grades for labs and so we may not need to grant a concession.)

## Missed Exams

- If you miss a quiz during the term — for any reason, including varsity sports — then you will simply make up for it during the final exam. (You do not have to let us know in advance about missing a quiz.)
- If you miss the final exam then you should request a deferred standing from Engineering Academic Services, and they will grant a deferred standing on a case-by-case basis. You will then write an alternative final exam, typically in the following summer session.

# Reporting Final Grades

The Department of Electrical and Computer Engineering has a review process for grades across all courses at the end of each academic term. Course grades will be released only after the review is complete and this may mean that grades are not available until late December or the first day of the January term.

In cases of academic misconduct, grades may be revised after the misconduct proceedings conclude.

# Guidelines and Advice

# Course Communication

**We will use Piazza for all course-related communication.**

### Contacting Course Staff

The course staff is here to help you. The staff is good at problem-solving, but terrible at reading minds; so please help us out by asking a question if something is not clear. Furthermore, please tell us when there is a problem. Feedback will improve the course … We can fix many problems, but only if we know about them.

To reach the course staff, please use Piazza under the appropriate topic. Do not send us an email!

In general, do not contact just one particular staff member, since that staff member may be busy, may not know the answer to your question, etc. You will get a quicker answer by contacting the entire staff. And, you may get an even quicker answer by posting publicly, where both your classmates and the staff can help you. In general, private posts to the teaching team should be reserved only for communicating on confidential matters.

TAs review questions several times a day rather than monitoring continuously, so please be patient while waiting for a response.

### Using Piazza

We encourage all members of the class to help one another on Piazza.

**Using the Correct Topic (Sub-)Folder**

When you make on a post on Piazza, you will be prompted to select a folder: This is Piazza's way of organizing your question by topic. Some folders like `logistics` have no sub-folders while others like `labs` have sub-folders, e.g., `lab1`, `lab2`, etc. *You should use the most specific folder that aligns with your question.* For instance, a question about Lab 1 should be put in the `lab1` folder and *not* the `labs` folder. However, a question about the meeting times for the labs or the general grading scheme for all labs should be placed under the `labs` folder. Correctly indexing your question will help you get a response from the teaching team as fast as possible.


**Private Posts**

You may make private posts on Piazza that are only visible to instructors and TAs. Private posts are only for matters containing confidential information about grades, health, specific questions about a solution to the assignments. All other questions should be made public.

*Where a private post is not justified, your post will be made public by teaching team.* This helps ensure that information and knowledge is fairly spread to the entire class.

**No Questions Will be Answered within 24 Hours of a Submission Deadline**

No questions regarding an assessment will be answered by the teaching team within **24 hours** of the assessment's submission deadline. Such posts will receive a generic reply to this effect:

*We will not answer this question as it was posted within 24 hours of the submission deadline as per the course policy.*

**Piazza Question Response Time Expectations**

If you ask a question on Piazza, we will try our best to answer your question within 48 hours. However, *weekends and holidays* *pause the response time clock.* So, a question posted on Friday at 6:00 pm would be answered by Monday at 6:00 pm, assuming the Friday and Monday are both regular business days.

**Student Answers** 

If someone asks a question to which you know the answer, then *please answer it*. Helpful, friendly replies are appreciated. You are, of course, not expected to give away answers to questions on assignments. *Answering other student questions is a great way to learn!*

**Do not Post Code/Solutions**

Do not post your code for programming assignments on Piazza — in particular, it is not acceptable to post code that you have written (whether correct or incorrect) or code that was not presented in class or made available to all students. It is okay to post the code that we’ve provided to all students, and use that as a starting point for discussions.

**Miscellaneous Guidelines**

If you have trouble, you are likely to find it helpful to read through the discussions on Piazza. Please do not repeat questions that have already been asked or answered there; search before you post.

To help your classmates, please do not post content-free “noise” messages saying just “Thanks for the post” or “You’re welcome” or “Me, too” — we have had complaints about them cluttering the forum. (One can often indicate that an answer is good by clicking on the good answer link.)

Questions perceived as abuse of course staff or fellow students will be tagged, with potential disciplinary consequences (including ban from Piazza and escalation to the Faculty of Applied Science).

### How to Ask for Help

We want to help you by answering your questions! We would much rather that you ask us than that you waste your time in confusion and frustration. Here we suggest some ways to make your question more likely to elicit a useful answer. The two key points are to explain what you know and to explain what you have tried. You may benefit from reading [this note on how to ask a good question](https://codeblog.jonskeet.uk/2010/08/29/writing-the-perfect-question/).

If you are having trouble with a tool or with code, then be sure to include all the relevant information, and to be precise, so that others can help you. State exactly what you did that caused the problem; this might be an action in a GUI or a command run from the command line. Also, state the exact outcome or output (not just “it gave an error”, for example), such as giving all the text from a popup message, or cut-and-pasting all the output from the command line. If your message is to the course staff, then commit your work to your GitHub repository so that they can reproduce the problem.

It can be helpful (to you and to others) to create the smallest possible test case that reproduces the problem. This helps to avoid being distracted by irrelevant details. You can proceed by binary search: cut away half of the input or the program at a time until you have isolated the problem. Even if you cannot do this, do still ask your question.

If you are having trouble with a concept, then please explain as much as you already understand. Saying “I don’t understand anything about X” is unlikely to be true, and unlikely to be helpful in clearing up your confusion. For example, explicitly answering these questions can be a good place to start:

- What problem is being solved?
- Why is this an important problem?
- What is wrong with other approaches?
- Do you understand all the terminology?
- Where have you looked for the answer?

For any question, an excellent approach is to logically explain why your problem seems impossible. If your code is giving a wrong answer, then state a detailed logical argument about why the observed output is impossible. If you cannot understand a statement in the readings or in lecture, then state why it is a logical contradiction (or why it is not relevant, or what part of it just makes no sense). Also, be specific about what confuses you — for instance, give a page number.

It is essential to say where you have already looked — in what books or handouts, what web search (Google is often smarter than the course staff and your friends), etc. Even if you do not discover your problem, this will help others to quickly understand the confusion — for example, perhaps you are misunderstanding a particular term, or you have forgotten to account for aliasing. And, it will prevent people from suggesting something you have already tried — such an answer delays you getting the help you want.

The above may sound like you should not ask a question until after you have at least tried to solve it yourself. As a general rule, that is actually good advice: sometimes you will solve it on your own and, in any case, you can provide much better information about the problem. That information will make it much more likely that you quickly get a useful answer. Otherwise, someone might just suggest something you have already done, or might be confused about your problem.

It is great to make some headway on your problem before asking a question. But, stop when you are no longer making headway! If you get stuck, then stop wasting your time and get help from someone else. We definitely don’t want you to waste your time in frustration, afraid to ask a question. Just explain what you know and what you have tried and ask the staff (or others) for help. Oftentimes there is a simple answer that can get you going again.

Finally, if you ask a question and later discover the answer, then please let everybody know! This will help others, and will prevent anyone from wasting time continuing to answer a moot question.

# Collaboration

- Discussion is encouraged!
- We expect highly ethical behaviour.
- Representing someone else’s work as your own is unacceptable.
- If you have a question about what is allowed, ask!

### Overview

For group projects, you are encouraged to collaborate with your partner(s) on all aspects of the work, and each of you is expected to contribute a roughly equal share to design and implementation. You may reuse designs, ideas and code from your own work earlier in the semester (even if it was done in a team project with a different partner). You may also use material from external sources, so long as: (1) the material is available to all students in the class; (2) you give proper attribution; and (3) the assignment itself allows it. In particular, if the assignment says “implement X,” then you must create your own X, not reuse someone else’s. Finally, your team may not reuse designs, ideas, or code created by other teams, in this term or previous terms.

When individual work is expected in an assignment: You are encouraged to discuss approaches with other students but your code and your write-up must be your own. You should not make use of any written solutions or partial solutions produced by others. Material from external sources can also be used with proper attribution, but only if the assignment allows it. You may not use materials produced as coursework by other students in the course, whether in this term or previous terms, nor may you provide work for other students to use.

To successfully build a large software system requires collaboration among people who have strong individual skills. You should actively discuss, divide work and share code within your group. The remainder of this collaboration policy pertains to discussions with people outside your assigned work group.

### Discussion is permitted, indeed, encouraged!

You can learn a lot from others; you can avoid getting stuck; and teaching someone else can be the best way to cement your own understanding. You may have discussions with anyone you like, including other CPEN 221 students.

No materials you bring to or take away from such meetings may be turned in as (part of) your solution. In particular, you may not bring any of your code or solutions to the meeting. You may only bring away information in your long-term memory. You must destroy any materials that you and others create during the meeting. Then, you must spend at least half an hour without thinking about CPEN 221. (Watching a mindless TV show is a canonical example; this is commonly called the Gilligan’s Island rule.) After that, you can use whatever you still remember.

### What You Should and Should Not Do

- You must write up anything you submit on your own.
- Your code (which includes tests and documentation), problem answers, etc. must represent your own understanding, as explained solely by you.
- You may not view other people’s code or solutions.
- You may not share any of your own code (including, as always, tests and documentation) with others, including bringing it to a meeting with others.
- You may not allow anyone except the course staff access to your CPEN 221 GitHub repository or any other location where you keep CPEN 221 code. Learn how to use your operating system’s access control mechanism.
- Do not post large amounts of your code (more than about 5 lines) to the course discussion forum.
- As an exception to the prohibition against viewing another student’s work, you are permitted to assist another student with tool-related problems (such as difficulty using IntelliJ or Git/GitHub), even if such assistance results in incidental viewing of code snippets. But, regardless, each student is expected to write and debug the assignment code individually.
- Debugging your code is not a tool-related problem.
- You may not represent someone else’s work as your own. You must give credit where credit is due. When you turn in assignments, you must list everyone with whom you’ve had substantive discussions. Likewise, if you obtained a key idea from some other resource, such as a textbook or a website, then you should credit it.
- You may not view and/or use any substantive material or solutions from similar assignments this term or previous terms at UBC or elsewhere, including anywhere on the Internet, transcribing solutions from any other source, etc.

Familiarise yourself with the [UBC policies on academic honesty](http://www.calendar.ubc.ca/vancouver/index.cfm?tree=3,286,0,0). If you have a question about what is allowed, ask the staff!

These guidelines are intended to convey the spirit of the law, fully understanding that the letter of the law may not cover everything that someone may think of. It is not effective for us to try to define a list of all impermissible activities. This approach can tempt people to look for loopholes.

It is your responsibility to satisfy both the letter and the spirit of the rules. If any part of this policy is not clear, or if you have any questions or concerns, ask for clarification. It is about your integrity, not just your CPEN 221 grade.

Integrity is crucial to a working engineer. Computing is at the core of almost all societal systems, and its discrete nature makes it especially unforgiving. Software has been responsible for death and damage. If you cut corners in your work, or are unprepared for it, then you, too, could cause such problems.

We expect you to show high ethical standards in CPEN 221, and in the rest of your career. Accordingly, violation of academic honesty (for instance, by cheating or by collaboration beyond what is permitted) will be taken very seriously. Violating the collaboration policy may result in failing the class and/or other penalties. A baseline penalty is receiving a 0 on the assignment on which you cheated. The instructors have the discretion to impose greater or lesser penalties than the baseline.

We will use technological and other means to detect cheating.

### Summary of Collaborations

|                                    |                              |              |            |             |       |
| ---------------------------------- | ---------------------------- | ------------ | ---------- | ----------- | ----- |
| activity                           | your partners in group tasks | course staff | classmates | AI chatbots | other |
| discuss concepts with ...          | ✔                            | ✔            | ✔          | ✔           | ✔     |
| acknowledge collaboration with ... | ✔                            | ✔            | ✔          | ✔           | ✔     |
| expose solutions to ...            | ✔                            | ✔            | no         | no          | no    |
| view solutions from ...            | ✔                            | no           | no         | maybe       | no    |
| plagiarise code from ...           | no                           | no           | no         | no          | no    |

# Teamwork

Teamwork is a crucial part of many professional and vocational activities. In a professional setting, a team works together to accomplish a task. In a broader societal context, team work is integral to making informed, democratic decisions and performing suitable actions.

### Why is it important for students to learn teamwork skills?

Students have different ways of learning and teamwork often helps students’ metacognitive awareness. Teamwork enables students to bring their ideas together thus leading to more creative thinking and enabling them to find solutions to problems – 'two heads are better than one’.

Teamwork activities develop management skills amongst students such as:

- organizational skills;
- communication skills.

Teamwork activities can:

- accommodate different personality types;
- accommodate for different ability levels amongst team members.

Teamwork develops lifelong learning skills which will be desirable attributes for future employment.

In the workforce people take on different roles and an understanding of preferred ways to contribute to a team is crucial for succeeding at work.

### What are some of the downsides of working alone?

Software construction is an activity that involves learning new skills continuously and adapting to new situations rapidly. In this context, there are some significant limitations to working alone.

Working alone reduces learning. One part of this is related to the first point, where there are fewer people with a shared context to challenge your ideas. Another is that because the project takes much longer to complete, each individual working along works on fewer projects over time.

Working on a team increases the bus factor for a project. The bus factor of a project refers to the number of team members that can be hit by a bus (or gets sick, leaves the company, goes on maternity leave, etc.) before a project comes to a complete halt; a higher bus factor reduces risk on a project. It also helps prevent obscure and undocumented shortcuts taken by a single individual and forces team members to spread knowledge and to do things in a way that other people on the team can pick up if necessary.

Working on a team increases accountability. Peer pressure is a powerful force. Particularly if you’re working with people whom you respect and don’t want to let down, the motivation to help your team succeed can override the dips in motivation that you encounter on days when you’re not at your best.

Slower project momentum from working alone reduces morale. Project estimation is hard, and projects tend to slip behind schedule. In single-person projects, a single stall can put the project to a halt, just like how in a grocery store with only one checkout line, one problematic customer or one item that needs a price check can put all sales to a temporary halt. With at least one additional person on the project, there can still at least be some forward momentum. A related point is that people tend to think about time spent on a project in terms of time elapsed and not time invested, so even if you’ve only been working part-time on a project for two months spread out over half a year, it’s hard for you and others within the organisation to internalise that and not think the entire project proceeded slowly and took half a year to complete. This disappointment at the time elapsed to a finish a project can also reduce overall morale and excitement.

The lows of a project are more demoralising when working alone. Sand traps that you struggle to get out of, monotonous work that you need to grind through, and bugs that seem to defy all understanding become less draining and more bearable when there’s someone else to share the pain with.

The highs of a project are more motivating when working as a team. Celebrating an achievement with teammates is a great way to boost morale. If you work alone, who are you going to high-five when you get something working?

### Teaching your teammates

In certain teams it is possible that someone has to teach others in the team because of varied experiences and backgrounds. Even when one is not an expert on a topic, there is enormous value in helping someone else learn.

### You don’t have to be an expert first.

It’s okay to not have all the answers, and it’s okay to be wrong. Framing the process as “sharing what you know” gives you more leeway to feel comfortable making mistakes, changing your mind, and sharing your knowledge in the context of your own experiences. It doesn’t make it any less valuable to your “students”, but it can make it easier to get started.

### You learn better by teaching others.

Another reason you shouldn’t wait to start teaching others is that it will help you learn. Research has shown that when we explain something to other people, we come to understand it better ourselves. The process of teaching others helps us recognize gaps in our own understanding and better organise information in our minds.

We’re also better at taking in the information initially, when we’ve been primed to think we’ll be teaching it to someone else later. It seems that this comes from a different way of approaching the learning material. We know we need to pay attention to the most important points and organise them in our minds, if we’re going to teach someone else.

It’s even been shown – to some extent – that first-born children are generally more intelligent than their younger brothers and sisters—potentially due to their efforts to share knowledge with younger siblings.

So, if nothing else, teach others for your own sake. You’ll reap the benefits in your own learning progress, regardless of whether you’re helping others (yet) or not.

### Teaching builds your reputation.

Don’t worry about whether you’ve hit “expert” status yet, or how big (or small) your audience is. Focus on what you’ve learned, or what you’re learning right now, and how you can share those lessons in a way that will help others. If it helps, imagine you’re teaching your former self, before you’d learned these lessons.

### How to work as a team in CPEN 221?

The projects in CPEN 221 are vehicles to promote teamwork (apart from helping you learn key concepts and practices).

According to concepts from organizational behaviour, there are five stages of team development: forming, storming, norming, performing, and adjourning. During the forming stage, teams tend to communicate in indirect polite ways rather than more directly. The storming stage, characterized by conflict, can often be productive, but may consume excessive amounts of time and energy. In this stage it is important to listen well for differing expectations. Next, during the norming stage, teams formulate roles and standards, increasing trust and communication. This norming stage is characterized by agreement on procedures, reduction in role ambiguity, and increased “we-ness” or unity. These developments generally are precursors to the performing stage, during which teams achieve their goals, are highly task oriented, and focus on performance and production. When the task has been completed, the team adjourns.

To accelerate a team’s development, a team contract is generated to establish procedures and roles in order to move the team more quickly into the performing stage. This process of generating a team contract can actually help jump-start a group’s collaborative efforts by immediately focusing the team members on a definite task. The group members must communicate and negotiate in order to identify the quality of work they all wish to achieve, and the level of group participation and individual accountability they all feel comfortable with.

Successful team performance depends on personal individual accountability. In a team environment, individuals are usually effectively motivated to maximize their own rewards and minimize their own costs. However, conflicts can arise when individualistic motives or behaviours disrupt team-oriented goals. For example, conflict can stem from an unequal division of resources. When team members believe they are receiving too little for what they are giving, they sometimes reduce their effort and turn in work of lower quality. Such “free riding” occurs most frequently when individual contributions are combined into a single product or performance, and individual effort is perceived as unequal. At this point, some individual team members may take on extra responsibilities while other team members may reduce their own efforts or withdraw from the team completely. These behaviours may engender anger, frustration, or isolation—resulting in a dysfunctional team and poor quality of work. However, with a well-formulated team contract, such obstacles can usually be avoided.


# How to Succeed in CPEN 221

CPEN 221 is intended to lay the foundation for a successful career working with software systems. Even if you do not foresee working with software systems in the future, you will learn some fundamental principles for managing the complexity that is inherent in any enterprise. In this missive, we will discuss how one might maximize their learning in this course and also address some common questions that have come up in the past and are very likely to be relevant to new students.

## Programming Fluency

CPEN 221 requires basic programming fluency. By fluency we mean comfort in writing programs in some language. We use Java as the programming language in this course, but having prior experience with any other language is a good starting point.

If you know essential programming constructs (selection and iteration), and can work with primitive datatypes (int, float, char, etc. in C) and arrays of primitive types then you should be able to keep pace with the material in CPEN 221.

Learning a new language is sometimes difficult, but one can navigate this task by separating the high-level problem-solving approach from the syntax of a particular language. Once you do this, you can take the solution approach and find the appropriate language features you need to use. Suppose you know C and can articulate a solution in C. You can then map that code to Java with the CPEN 221 onboarding guides provided with the course, which cover the required Java 25 language material and development tools. The [current Java references](#books) below can answer more detailed questions. You can also practise short Java problems at [CodingBat](https://codingbat.com/java).

It may not appear so during the term, but most former students attest to the need for learning aspects of a programming language on their own — and in a short timespan — as one of the major benefits of CPEN 221.

## **About the Course Structure**

Practice and feedback are key to learning. We have created course activities that provide you many opportunities to learn:

- lab activities
- mini-projects


If you utilize the opportunities then you will accelerate your learning.

We will also spend a lot of time when we meet discussing material, but not in the form of a traditional lecture. There are times when a traditional lecture is useful but less so in a course where we want to emphasize principles and see you translate these ideas into practice.

**References**

1. [Course Transformation Guide](http://www.cwsei.ubc.ca/resources/files/CourseTransformationGuide_CWSEI_CU-SEI.pdf), Carl Wieman Science Education Initiative
2. [Improved Learning in a Large-Enrollment Physics Class](http://science.sciencemag.org/content/332/6031/862.full), Deslauriers, Schelew, Wieman

## Readings

Why do I need to do the readings at all? The readings are the primary medium for communicating the conceptual material in this course. The lectures are meant to motivate the theory, provide a seasoned perspective from the instructors’ experience, explore key ideas, and perform demonstrations. Current & former teaching assistants have noted that it is impossible to do well on the theoretical component of the course without doing the readings.

Why do I need to complete the readings before class? Since doing the readings at some point is necessary, you may as well do them before class, because that’s when it is most time efficient for your learning. Reading the material before a class meeting allows you to reflect on the content first so that you can discuss confusing aspects and so that you can see how ideas are translated into practice. Reading in advance adds thinking time: time to formulate questions and partial answers, as well as to permit repeated exposure to the material.

**Reference: [The Spacing Effect](https://en.wikipedia.org/wiki/Spacing_effect)**

One of the tragicomic statements that was part of the student feedback to this course from a couple of years ago was that there was too much reading and that "... we are engineers not readers". There are several ways to respond to this comment. But one of the main threads in the response has to do with the role of reading in software engineering. Programming is a creative task. The end goals are often to build a working system when the requirements are expressed informally, in a natural language, by people (colleagues, users, clients). If software engineers cannot read carefully, they cannot understand what they have to do. They will not realize that there are holes that need to be filled in. (A big barrier to writing good software is unstated assumptions -- and much of this course is about overcoming that hurdle.) Their code will not meet the need, and it will behave unexpectedly. And then a programmer may smooth over a gap in a way that does not match the unexpressed desires of the user. As professors, one of the most common problems we encounter is that students who think they know to program fail to read and interpret correctly a carefully crafted problem statement. They would sometimes complain that the statement was confusing, but the reality was that the statements they complained about were, for the most part, complete and unambiguous. The same need for rigorous, analytic reading pervades many facets of system building: interpreting requirements, protocol specifications, algorithm definitions, and language and API documentation.

## Laptops in the Classroom

You can use laptops when needed but — unless you are told to open up your laptops — they should usually remain closed. Your laptop, and even your smartphone, is a huge opportunity for distraction. And the price for this distraction will be paid not just by you but by those all around you.

A study found that:

- For note-takers with laptops, multi-tasking led to an 11% drop in comprehension test scores.
- For note-takers without laptops, merely having a laptop multi-tasker in their field of view led to a 17% drop in comprehension test scores!

If you want to use a smartphone in your lap, so that the screen is not visible and not distracting to others, you will still be hurting yourself.

**References:**

1. [Laptop multitasking hinders classroom learning for both users and nearby peers](http://www.sciencedirect.com/science/article/pii/S0360131512002254), Sana et al.
2. [The Pen Is Mightier Than the Keyboard: Advantages of Longhand Over Laptop Note Taking](http://pss.sagepub.com/content/25/6/1159.full), Mueller and Oppenheimer

## Programming Tools

"The tools we use have a profound and devious influence on our thinking habits, and therefore on our thinking abilities." — Dijkstra

We will introduce you to several tools in this course. IntelliJ IDEA, JUnit and Git are the top three tools that you will likely use. Mastering some tools will improve your productivity as a programmer. By introducing you to the tools and expecting a minimum level of use, we hope to put you on the path to mastery. Do not let the tools overwhelm you, and at the same time work towards using each tool effectively.

Having used a distributed source code control system such as Git makes it easier to adjust to other tools that have the same purpose. For example, your co-op employer may be using [Mercurial](https://www.mercurial-scm.org/), which is another distributed source control management system. It does help to understand why you need the tools first so investigate for yourself. Do some reading.

## Java vs. Software Construction Principles

The overarching theme is good software construction practices. It may appear that there is more about Java but this is incidental to the process of learning both the principles and the language at the same time. But -- we do not want to have people start with bad habits so we favour this approach. When you are programming, make the effort to connect what you are doing to the course concepts: this will happen when you are not thinking only about syntax.

## How to Become a Good Programmer

Achieving excellence in any activity takes time but there are few things you should plan to do.

1. Enjoy it!
2. Do it!
3. Talk to programmers.
4. Work on projects with other programmers.
5. Work on projects after other programmers. See if you can make things better.
6. Become comfortable with many languages. At least one of the languages you know should be a functional programming language.
7. Understand the computer: how does it execute a program?

## Hints for Success in CPEN 221

1. Start on assignments early. We cannot emphasise this enough.
2. Understand the problem you are trying to solve using software. Decompose the problem into parts. Sketch a high-level solution on paper. Then write code - on a computer. You do not need to draw formal flowcharts; clear notes are often sufficient.
3. Learn to read code. Start with the examples we provide.
4. Learn to read software documentation. Use [dev.java](https://dev.java/learn/) for explanatory material and the [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/index.html) to determine what library types and methods provide.
5. You are working almost entirely with man-made artifacts. Try to understand the design choices that the programming language creators made. A program is simply some lines of (mostly) English text: think about how a computer is made to understand this text.
6. Ask for help if you are stuck. The course staff are here to support you. Use office hours and the course discussion forum wisely. When you ask for help, be prepared to explain what you have done so far.
7. Do not fear to write code that will not work and then to debug the code. You will learn more from that experience than from suggestions people may provide to avoid problems.

## Different Courses Have Different Contexts

In addition to the overall increase in software-driven automation around us, the practice of developing software that you learn now is something that you will take with you to a job. You will engage in similar discussions on how to construct good software in a workplace. This extension to the workplace is somewhat different from the critical thinking and understanding that you gain in other courses, e.g., mathematics, physics, circuit analysis. In those other courses, much of what you learn is actually automated in practice, and you would use design tools that hide routine computations. The learning from a course like CPEN 221 (or, for that matter, CPEN 211) is about both principles and practice, whereas the emphasis in some other courses would only be the scientific and mathematical principles. As a consequence, you should expect a palpable difference in the "feel" of this course when you compare it to some other courses. This comment is not intended to downplay other courses (they are important; for example, the rigour of MATH 220 will help you understand some aspects of CPEN 221 better) but to indicate the difference in expectations.

## Motivation

Remember that you have chosen fields of engineering that rely heavily on software systems. Even if you see yourself as a physicist, you may want to keep in mind that some of the most recent developments in the physical and chemical sciences are a result of software models and simulations of the real world. The 2013 Nobel Prize in Chemistry was awarded for [computational chemistry](http://blogs.scientificamerican.com/the-curious-wavefunction/computational-chemistry-wins-2013-nobel-prize-in-chemistry/). Software solutions are guiding the design of new drugs, for example. Hopefully, you do not want poor software construction to lead to mistakes in drug production!

Stay motivated: [the payoff is worthwhile](http://www.wsj.com/articles/SB10001424053111903480904576512250915629460).

**Related Reading**

- [Beating the Averages](http://www.paulgraham.com/avg.html), Paul Graham
- [How to Become a Hacker](http://catb.org/~esr/faqs/hacker-howto.html), Eric Raymond
- [Scheming is Believing](https://sites.google.com/site/steveyegge2/scheming-is-believing), Steve Yegge
- [Teach Yourself Programming in 10 Years](http://norvig.com/21-days.html), Peter Norvig
- [Confusion in Comprehending Code](https://cpen221ubc.notion.site/Confusion-in-Comprehending-Code-05043900d6b6404bb36fa8443b35bc09?pvs=4), CPEN 221 staff


# Books

The course readings are the textbook for CPEN 221. You do not need to buy another
book. The resources below are references and extensions: choose one that matches
the question you are trying to answer.

## Closest companion

[Martin P. Robillard, *Introduction to Software Design with Java*, third edition
(2026)](https://link.springer.com/book/9783032118202) is the closest companion to
the course. It treats design through encapsulation, interfaces, state, testing,
composition, inheritance, and functional techniques using current Java. The CPEN
221 readings remain the authority for course terminology, specifications,
representation invariants, concurrency, and assessment expectations.

## Books by purpose

| If you need… | Read… | Keep in mind… |
|---|---|---|
| a compact Java 25 reference | Benjamin J. Evans, Jason R. Clark, and David Flanagan, [*Java in a Nutshell*, ninth edition (2026)](https://www.oreilly.com/library/view/java-in-a/0642572255992/) | Use it to look up the language and core libraries, not as a cover-to-cover course text. |
| a more detailed Java 25 reference | Cay S. Horstmann, [*Core Java, Volume I: Fundamentals*, fourteenth edition (2026)](https://www.informit.com/store/core-java-vol.-i-fundamentals-9780135558577) | It is thorough and substantially longer than this course requires. |
| stronger testing technique | Maurício Aniche, [*Effective Software Testing* (2022)](https://www.oreilly.com/library/view/effective-software-testing/9781633439931/) | Especially relevant for specification-based tests, boundaries, and property-based testing. |
| deeper foundations for specifications and data abstraction | Barbara Liskov and John Guttag, [*Program Development in Java* (2000)](https://www.oreilly.com/library/view/program-development-in/9780768685299/) | Read selected conceptual chapters. Its Java syntax and libraries are historical. |
| short essays on Java API and class design | Joshua Bloch, [*Effective Java*, third edition (2018)](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/) | Read selected items. It covers Java 8 and 9, so check current Java 25 documentation. |
| techniques for improving existing code | Martin Fowler, [*Refactoring*, second edition (2018)](https://martinfowler.com/books/refactoring.html) | The design ideas transfer to Java, although the second edition's examples use JavaScript. |
| another view of modular design | John Ousterhout, [*A Philosophy of Software Design*, second edition (2021)](https://web.stanford.edu/~ouster/cgi-bin/aposd.php) | Treat it as an argued design position, not a rulebook. The free [Ousterhout–Martin design debate](https://github.com/johnousterhout/aposd-vs-clean-code) makes the disagreements explicit. |
| engineering practices for long-lived code | Titus Winters, Tom Manshreck, and Hyrum Wright, [*Software Engineering at Google* (2020)](https://abseil.io/resources/swe-book) | The complete book is free online. Separate broadly useful principles from practices that depend on Google's scale. |
| a disciplined approach to recursive programs | Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, and Shriram Krishnamurthi, [*How to Design Programs*, second edition](https://htdp.org/2022-2-9/Book/index.html) | The book is free online and develops a useful design recipe, but its examples use Racket rather than Java. |
| systematic debugging experiments | Andreas Zeller, [*The Debugging Book*](https://www.debuggingbook.org/) | The book is free and interactive. Its examples use Python; focus on the language-independent techniques. |
| a next step after CPEN 221 | Martin Kleppmann and Chris Riccomini, [*Designing Data-Intensive Applications*, second edition (2026)](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) | This is an advanced systems book, not a companion for weekly course material. |

## Authoritative online references

Use [dev.java](https://dev.java/learn/) when you need an explanation of a Java
feature. Use the [Java SE 25 API](https://docs.oracle.com/en/java/javase/25/docs/api/index.html)
for library contracts and the [Java SE 25 specifications](https://docs.oracle.com/en/java/javase/25/docs/specs/index.html)
when exact language or JVM behaviour matters. The course uses JUnit 6.1.3; its
[versioned documentation](https://docs.junit.org/6.1.3/overview.html) matches the
examples and build files used in Fall 2026.

## Access

Before buying a book, check [O’Reilly for Higher Education through the UBC
Library](https://guides.library.ubc.ca/az/oreilly-for-higher-education). UBC provides access to
the titles on that service; sign in with your CWL when prompted. Several books in
this list are also available directly from their authors or publishers.

# Land Acknowledgement

This course is held on the UBC Point Grey (Vancouver) campus, which sits on the traditional, ancestral, unceded territory of the Coast Salish Peoples, including xʷməθkʷəy̓əm (Musqueam) First Nation, Squamish, Tsleil-Waututh, Stz'uminus, and Stó:lō First Nations.

UBC is implementing its Indigenous Strategic Plan, taking a leading role in the advancement of Indigenous peoples’ human rights. To learn more about the Faculty of Applied Science’s role in building upon the Indigenous Strategic Plan and committing to Truth and Reconciliation, please visit:

[Equity, Diversity, Inclusion + Indigeneity (EDI.I) \| UBC Applied Science](https://apsc.ubc.ca/EDI.I)
