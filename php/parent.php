<?php
// A Task is just a class which contains information about something which must be done.
class Task {
    var $title = "";
    var $assignee = "";
    public function __construct($title, $assignee) {
        $this->title = $title;
        $this->assignee = $assignee;
    }
    public function getAssignee() {
        return $this->assignee;
    }
    public function getTitle() {
        return $this->title;
    }
}
$myTask = new Task("Do the thing!", "Adrian");
// var_dump($myTask->getTitle());
// string(0) "Do the thing!"
// var_dump($myTask->getAssignee());
// string(0) "Adrian"
// A Todo contains the same information as a Task, but also whether or not that Task has been finished.
class Todo extends Task {
    var $isFinished = false;
    public function __construct($title, $assignee, $isFinished = false) {
        parent::__construct($title, $assignee);
        $this->status = $isFinished;
    }
    public function getIsFinished() {
        return $this->isFinished;
    }
    public function complete() {
        $this->isFinished = true;
    }
}
$myTodo = new Todo("Do the other thing!", "Michael");
var_dump($myTodo->getIsFinished());
// bool(false)
$myTodo->complete();
var_dump($myTodo->getIsFinished());
// bool(true)
var_dump($myTodo->getAssignee());
// string(0) ""


// Despite the fact that the Todo class extends the Task class, the assignee varaible
// remains empty. Why?