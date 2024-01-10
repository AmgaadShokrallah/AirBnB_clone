 readme file for AirBnB clone project.

Background Context
Welcome to the AirBnB clone project!

Before starting, please read the AirBnB concept page.
First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
    create the first abstracted storage engine of the project: File storage.
    create all unittests to validate all our classes and storage engine

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on my server a simple copy of the AirBnB website.
i won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, i will have a complete web application composed by:

    A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
    A website (the front-end) that shows the final product to everybody: static and dynamic
    A database or files that store data (data = objects)
    An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

command interpreter:
		Create a new object (ex: a new User or a new Place)
		Retrieve an object from a file, a database etc…
		Do operations on objects (count, compute stats, etc…)
		Update attributes of an object
		Destroy an object

