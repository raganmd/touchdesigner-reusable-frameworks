# Reusable Frameworks
Authoring large projects in TouchDeisgner is an interesting proposition. It's often easy to get your first project up off the ground, but by your 10th, or 20th you soon find that there might be an awful lot of repetition in the work that you're doing. In fact, like it or not there's a good chance you loose a lot of time to setting up the same things over and over again. Hopefully you're learning lessons along the way about pieces that are more or less efficient, or about how you like to work... but how do you make it better? What are some essential principles we can hold onto? What are some best practices that we should keep in mind? How might we stop doing the same pieces over and over again, and make more time for the fun stuff - the art making and the creative pieces?

That's what we'll aim to explore in this Repo, and the posts that are connected.

#### *A Disclaimer*
This is just one way to work. It's not the best way, or the "right" way, or anything of the sort. It is instead the most essential elements I'd offer to intermediate TouchDesigner programmers who want to reduce the amount of labor that goes into setting up a project, and instead want to focus on making more impactful art. Configuration and architecture is an art in itself - there's a style and form to this process, and you dearest reader / developer / artist / wanderer will likely find your own way in this process. My hope is that this will be a lesson in map making so that you can make your own.

## Assumptions
I'm sorry, but I've made some assumptions about who is reading this. 

I have had to assume that you're familiar with TouchDesigner, and that you've used it to at least an intermediary extent. "Slick Matt - I did a demo and a class project once, so I'm ready." Slow down there tiger. My assumption here is that you're more like 12-24 months into your TouchDesigner adventure. That you've done a few gigs, some paid gigs, and maybe even have an installation or two out in the wild. That likely means that while you are still experimenting with architecture, you have a starting idea of how you'd organize a project - better still, you have a repeatable way you've started to organize your projects. 

I'm going to assume that you've also got a handle on Python. You don't have to be a Pythonista, or a lvl 80 Python Mage - but if you find yourself still fighting with single line scripts (and we all have) this is going to feel like the very deep end of the pool. This is your proceed with caution heads up - it may feel like it gets intimidating very quickly, and I don't want you to feel discouraged. The good news is that there are a healthy set of Python in TouchDesigner pages that you can read to get up to speed. So don't stress, just take some time to level up a little - this series will wait for you.

UGH - Why should all that matter?! 

Well, it matters because it means you're past the real rodeo part of your development experience - the fly by the seat of your pants and make it work minutes before curtain parts of your journey. It's okay if you're not there yet; the intention of this kind of practice is to start a cultivated and mindful approach that makes room for you to focus on the parts that are really fun and interesting, while building regular structures for the rest. If you're not ready for that kind of practice (and I wasn't for a good chunk of time) that's okay - this series will be waiting for you when you are.

It matters because human beings are funny creatures - we can be resentful or resistant to ideas and practices that feel like impositions. This kind of practice will test you, it will require that you're invested in not what works for today, but in building something that will work for tomorrow and the day after. If you're not ready for the responsibility of owning a house, don't buy one... there will still be houses to buy when you're ready. 

Your mindset, and the spirit with which you approach these challenges matters - that's what I'm really getting at with the above. Some of this will be hard, or won't make sense, or will require you to practice. It will require that you're ready for those challenges - maybe not with a glad heart, but at least with a willing one. I'm assuming that if you've read this far, that you are ready for all of the above. Buckle up, it's gonna get fun.

## Objects 
You are already an object orient programmer if you've been using TouchDesigner. You might not fully understand the nature of OPP, or the language that goes along with, or even why it matters... but if you've been connecting boxes with little noodle lines, you've been working in an Object Oriented paradigm. That's important to recognize, because how we think of the component pieces that build Touch networks, can also help us think about how we might consider building re-usable and generalized pieces in our own work. 

The internet is full of rich and robust prose about what Object Oriented Programming is and isn't - I'm not going to re-write that tome. To help us at least share some ideas I will say just a few things about the idea of OPP. More than anything OPP is an idea - it's a construction for how to talk about and collaborate with machines - machines that happen to be terribly literal. OPP offers us squishy humans a conceptual frame for talking and thinking about the world in way that we can in turn translate into a language that can be interpreted by our silicone collaborators. No metaphor, however, is perfect - and the perils of the OPP exercise is the precarity of imagining that you can perfectly describe the world with this paradigm. Don't fall for that temptation. OPP is a kind of classification schema - an object-centric and "is-a" vision of the universe. Here I'm going to resist the temptation to classify it as "good" or "bad" and rather just offer a reminder that it is just an idea, what makes it powerful or useful is how we use it. 

An example to get us out of theory-ville USA. My partner and I live with two cats - Malcolm and Inra (yes, they are named after characters from FireFly - thank you for asking). Malcolm is a house cat, which is a cat, which is a mammal, which is an animal. Malcolm is a special instance of a house cat - but based on the above he should have shared properties and behaviors with other house cats... which are themselves a special kind of cat, which is a special kind of mammal, which is a special kind of animal. Why this all matters is because the very notion of objects in OPP is their ability to be generalized. An instance of an object is special - but we describe objects as being general abstract representations of an idea. 

 If you feel like you don't get it yet, that's okay... in fact that's probably better. what is important is to consider that the Russian Nesting Doll kind of notion here is that we can classify or describe the whole world and how it operates in this same hierarchical and tidy set of compartments. The world, of course, is not so fastidious - it is instead messy and chaotic; sometimes non-sensical and often unpredictable despite our best efforts. So when I say don't fall for the temptation that this kind of order offers; what I means is that this reducativist way of thinking about the world is just that - reductavist and imperfect. That doesn't meant we can't leverage this idea with some utility, but it would be dangerous for us to romanticize this concept too heavily.

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
What are my standard reusable pieces?!  
That's a hard question, and the structure I'd offer as a starting point falls into four primary blocks. Each of these will likely have additional blocks as well, but these form our top level structures. It's important to remember that these top level structures can/should/will be made up of other structures. I would also encourage you to remember that you won't get this right the first time, or the second, or the third. I'd encourage you to embrace the iterative nature of this process and acknowledge that a part of what you're likely chasing here is finding the right set of high level structures that's configurable to meet your specific needs. So where do you get started then? What are these mysterious puzzle pieces and what's a way to think about the role they fill? For starters let's organize our re-usable framework into the following:
* Communication (base)
* Output (container)
* Tools (base)
* Data (base)

You'll find that in the network I adhere to the practice of leaving the operator name as a prefix to my unique name, e.g. `base_someOtherNameHere`. This convention grew out of a long conversation with fellow developers at Obscura digital and seeks make the operator type as transparent as possible. When you're reading another developers Touch network it can often be difficult to quickly diagnose or determine what they're doing. Leaving operator names intact as a prefix can help ameliorate this gripe - you are in no way expected to do the same, but you should notice that it is a consistent property of the network example. I'm not a huge fan of the long operator names that happen when you leave the base name of the operator in place, but I would still recommend this practice. At the very minimum one practice to absolutely avoid would be to name operators as something they're not. What on earth could I possibly mean?! Well, imagine that you have an OSC in CHOP. You're doing some additional math and other logical operations so there is a long chain of operators that you connect your OSC in CHOP to before finally connecting it to a null CHOP. So far so good. Then you name the null CHOP `osc`. On the face of it that seems reasonable, it is the final stage of all of the osc data, and that is a descriptive name for tha operator - so at first blush it passes muster. Then you ask another developer for a second set of eyes on some problem you're having with the logic in your CHOP network. "Look at the OSC CHOP, I think the problem starts there..." Now we have a problem. Does your friend look at the osc in CHOP and the logic between the OSCin and the Null, or do they look at everything after the Null CHOP called `osc`? If you're lucky you're only a few slack messages away from clearing up this set of overlapping terms, at worst your collaborator has spent hours of dev time searching through the wrong parts of the project to try and help. That seems like an issue of convenience and style, but it's worth embracing the fact that names matter. When you're doing some final programming at 4 am before the client review, or in the frantic minutes when something has gone wrong you'll curse yourself for these kinds of things.

### Communication
*base_com*
Once you're working with multiple machines, multiple instances of TouchDesigner, or multiple interconnected applications you'll quickly find that you need to exchange messages. `base_com` is the epicenter of that function. The idea is to centralize the communication elements into this base, so rather than having OSC or TouchIn/Out ops spread hither and thither, they instead live in this component. There are some additional elements that have to go into play to control how you think about building in here, but the essential idea is that this houses any operators that do inter-application communication. That's hard to get used to, but makes sure that you always know where to look for messages coming in, or where to target for messages going out. In practice you'll also likely have several sub-components to handle talking with OSC, other touch projects, MIDI, and the like.

### Output
*container_output*
Output is just that - what the application is going to display. On the controller this is likely a UI, while on display nodes this is going to be some kind of screen or projector output. This is the hardest piece to build a mental model for, as this is a component that's likely different from machine to machine, or process to process. That might sound very strange, but the of the essential ideas behind buildng one toe file with multiple configurations has it's roots in understanding that the tox files that you load in any given instance of the application can be different. 

### Tools
*base_tools*
Tools are an excellent place to keep pieces pf functional code that are useful across machines. The save TOX from above is an excellent candidate for the Tools base. Maybe you have a performance monitor or a logging tool - this is a great place for those tools to end up. Tools are elements that you might use for the actual deployment of your project, or that you might only use during development to help streamline your process. Ideally these are components that have no extra cooking associated with them, or at the very least can be configured to not cook - you could always disable them, but ideally you have a custom parameter that turns off cooking.

### Data
*base_data*
Data is an excellent place to keep track of just that - data. Maybe you have a playlist or an assets folder that you use in your project - sounds like it belongs in Data. Maybe you're doing some projection mapping and you're using a 3D model based approach - that goes in Data. Like the components described above, this likely has a number of sub-components. A set of icons that has to be in every project - sounds like you need another base called Assets in your Data component. 

## Extensions
If you haven't yet started using extensions, it's well worth jumping into the deep end of the pool and to start working with them. Extensions are hands down one of the best ways to make major strides in your process and approach when it comes to TouchDesigner. If you're building your first VJ app this might not be for you yet... but if you've made a few projects and want to start consolidating your Python into diff-able and portable blocks - it's time to learn extensions. No excuses, you can do this. 

As a reminder, extensions give us a Pythonic mechanism for extending our code. Just like we can use dot properties on many of our Touch objects (op("some_moviefile_in).par.play = 1), extensions allow us to collapse otherwise complex logical operations into easier calls. If we were making a game we might think about what happens when the game is over - maybe we want to play some ending animation, then roll credits, allow the player to enter their initials for a high score, and on and on. Rather than writing some long sprawling set of operations, what if we could instead just do something like  `op.Gameop.End_game()`? That's what extensions allow us to do, and it saves a whole mountain of repeated work.

In the projects I've worked on, each of the major components in a network (like the ones above) all have their own extension. On top of that the project itself has an extension as well. You might well be feeling like that's a little extension heavy - and there's some truth to that... maybe. Programming isn't just an encoding of mathematics and logic, it's a philosophical activity. "Why this series of operations?" "Smaller tasks joined together, or larger complicated tasks?" One perspecitive here is that we want to use many sharp tools, rather than a single "do-everything" tool. You can certainly cook many fine meals using only knife - but most chefs use lots of knives in all variety of sizes, with all variety of blade types - curved, straight, seriated, etc. It's the same core idea here, you could do everything in a single extension - but doing that breaks one of the very problems we're aiming at solving... portability. Now every one of these externalized tox files needs our master extension in order to work - and that extension is gonna end up with a whole mountain of things in it that probably won't make sense for your next project. 

What if instead each of your tox files had an extension set that only addressed the functionality of that tox? That's the idea here. Now when you make some super sweet calibration process or blending approach it's easier to take from one project to another. That might not make sense right now, but after you practice a bit it will feel more and more natural. 

## Advanced Extensions - Inheritance
These days I use inheritance more and more in my extensions. In-hear-a-what-now? Just like genetic inheritance, a similar principle exists in programming paradigms. A trait or operation type can pass from one object to the next without having to re-write that from the ground up. So that's great... but why do I want that? If you're asking that question, you're not alone. It took me lots of grumbling and experimenting to really land on a place where inheritance makes sense to me in TouchDesigner. For me it lands right on the question of what feature do I need to write for this job, and what feature do I need to write for all jobs? For me, any given base might have a general extension, and a job extension. We might think about the circumstance where we're thinking about time - we almost always end up needing to stream time or a some kind of clock to all machines. For almost all jobs we need a way to stop, rewind, advance, or reset that clock. Those all sound like excellent functions for a general extension. But maybe we're working a job where we need to run the clock as a palindrome... which sounds silly, except that the client NEEEEEEDS IT. So we have to add it to the project, but if we add it to our general class then we have to remember to take it out later - something we'll forget to do until four or five projects from now when we can't figure out why this stupid Palindrome() method keeps causing some weird error... and as soon as we take it out, everything is broken for four hours while we track down all the stupid dependant tentacles of the function. Stupid.

Instead, we could just keep this stupidity in a separate extension that inherits all of the best parts of our previous work, while making room for us try out new ideas without mucking up the careful and thoughtful work we've done. It might seem obvious to you as you read this... but if it doesn't - don't worry, it will some day. 

## Configuration
"I don't need a configuration process." Sure you don't. I didn't, until I did... then boy did I ever. This is one of the least glamours but fundamentally essential elements in large format distributed work. Before we get in too deep, let's think about the challenge. You're working on a big job - 11 servers, 30+ projectors, and in a perfect world you'd have all the equipment up and running in wherehouse space so you can test to your heart's content. But we live in the real world, and the severs are back-ordered, or your buddy who is building them isn't gonna have any free cycles for 4 more weeks and you can't wait that long to start working. 

Okay. 

So what do you do?

Well, you could make a unique toe file for each server. That's not a terrible idea, but it means that you probably have a lot of copy pasta in your future. Maybe you'll make that a little better, and use external toxes for all your major components - so the skeleton stays the same and you only really have to work in a single file. That's not terrible. Until it's time to distribute updates. Then you have to reserve time in your schedule to getting files copied, then testing to make sure they're starting up correctly, and some time to fix / address the servers that aren't behaving for some reason. 

What if instead you had a config file that each machine checked at start-up, and based on an identifier it configured itself? Boy golly wouldn't that be nice? To make that happen we need a config file, and we need a config process to do all of this work. It's the first thing that happens when the project starts, and we need a graceful default state so we don't just fail on start-up if we haven't set-up the machine correctly first. As a bonus, it also means that we can tell any machine to change its configuration on demand. I've spent a lot of sleepless nights fighting with this problem, and while it's now obvious to me, it wasn't always. The learning curve here is steeper than you might want it to be, but that's okay. We've got a solid starting place we can pull apart to launch from.

### JSON


