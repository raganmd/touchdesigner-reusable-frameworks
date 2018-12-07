# Reusable Frameworks

Authoring large projects in TouchDeisgner is an interesting proposition. It's often easy to get your first project up off the ground, but by your 10th, or 20th you soon find that there might be an awful lot of repetition in the work that you're doing. In fact, like it or not there's a good chance you loose a lot of time to setting up the same things over and over again. Hopefully you're learning lessons along the way about pieces that are more or less efficient, or about how you like to work... but how do you make it better? What are some essential principles we can hold onto? What are some best practices that we should keep in mind? How might we stop doing the same pieces over and over agian, and make more time for the fun stuff - the art making and the creative pieces?

That's what we'll aim to explore in this Repo, and the posts that are connected.

#### *A Disclaimer*

This is just one way to work. It's not the best way, or the "right" way, or anything of the sort. It is instead the most essential elements I'd offer to intermediate TouchDesigner programmers who want to reduce the amount of labor that goes into setting up a project, and instead want to focus on making more impactful art. Configuration and architecture is an art in itself - there's a style and form to this process, and you dearest reader / developer / artist / wanderer will likely find your own way in this process. My hope is that this will be a lesson in map making so that you can make your own.

## Objects 

You are already an object orient programmer if you've been using TouchDesigner. You might not fully understand the nature of OPP, or the language that goes along with, or even why it matters... but if you've been connecting boxes with little noodle lines, you've been working in an Object Oriented paradigm. That's important to recognize, because how we think of the component pieces that build Touch networks, can also help us think about how we might consider building re-usable and generalized pieces in our own work. 

## TOX Files as Modules
Before we can dig into the essential pieces we'll be using, it's important to take a moment to talk about using `TOX` files as modules. If you've used other object oriented environments you're likely already familiar with the idea of modules - smaller components that may or may not have dependencies on other components. Our daily human lives are full of this concept - even if we use different words to convey that meaning.

I'm more of a kitchen metaphor human, than a car metaphor, so let's see if we can try one of these examples on for size. Let's say we're making a pie. A pie usually has a few essential components. It usually at least has crust and a filling. When we think about pie, we usually intuit that it has at least those essential parts. The crust might be made of pastry or ghram crackers, and the filling could be any number of things - coconut, chocolate, pumpkin, apple, etc. Regardless, our pie - whatever the kind - is made up of these components. Those components in their own right are made of ingredients (both components might even share ingredients). With any luck our pie is more than just a sum of its parts - hopefully it is delicious and wonderful, and not just a mash of haphazardly assembled food stuffs. That's an important idea, and one we easily take for granted - namely, that our final product is an assemblage of components.

That is seemingly obvious, but worth pondering - if only for a moment - because it is with that very idea that we'll start to build out a model of what we want to create a blueprint for how our projects work. The big picture idea here is that we want a framework that will serve most of our needs. We'll need some kind of crust, and some kind of filling, and and and. It's an imperfect model, but this idea gets us started thinking about how to approach this problem. You might find yourself asking the questions:
* is blank an ingredient, or a component? 
* is blank a different flavor of blank component, or a completely different kind of component?
* do I really need three different versions of this same component, or parameters to help control it?
* can I take this specific idea and make something more general out of it that I can configure across multiple projects?

With all of that in mind, we can stretch our imaginations to think about the fact that what we build will likely have several consistent parts or modules. They might come in different flavors or varieties (and in fact they likely will), but at the end of the day we should be able to identify the high level conceptual blocks that will make up our projects. 

Okay, so where does that fit in with thinking about using `TOX` files from TouchDesigner? A `TOX` is a kind of code block for TouchDesigner. This is a module component that you can drop into any network. This means we can make reusable and transportable modules that we can move from project to project. This also means we have a way of saving single modules rather than whole toe files. That's helpful / essential when it comes to working on teams as it means that two people can work on two different parts of a project at the same time, without breaking a source-control tool like git.  

In this example project we'll focus on how our essential project components can be packaged into TOX files, and why that's powerful.

Okay - but it's a lot of work to save `TOX` files and keep that all organized! And you're right for thinking that. Lucky for us you can use a little TOX module to help with this process that's already set up to streamline this process. You can find it here - [TouchDesigner-Save-External](https://github.com/raganmd/touchdesigner-save-external)

## Standard Reusable Pieces
What are my standard reusable pieces?! That's a hard question, and the structure I'd offer as a starting point falls into four primary blocks. Each of these will likely have additional blocks as well, but these form our top level structures. 

### Communication
*base_com*

### Output
*container_output*

### Tools
*base_tools*

### Data
*base_data*




## Configuration

### JSON


