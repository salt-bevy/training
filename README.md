# Training
Lessons about the use of Salt, salt-cloud, networking, and lots of other stuff.

This repository is designed to be installed next to the
[salt-bevy](https://github.com/salt-bevy/salt-bevy.git) repository,
and is nearly useless by itself.

These lesson are, in essence, a lab manual for training.
The [salt-bevy](https://github.com/salt-bevy/salt-bevy.git) repository
contains the actual lab upon which the lessons are based.

The salt-bevy software is designed to also be useful as a base
upon which to build a more complex network (bevy) of computers
suitable for production work. 
A production system would contain the salt-bevy repo, and its own repo,
but not these lessons.  
See the [advanced bevy master](lessons/advanced_bevy_master) lesson
which explains how to do that.
(In keeping with the old Python tradition, the example production system
is named for the famous [black knight](https://www.youtube.com/watch?v=2eMkth8FWno&t=6s).)

So, initially, for training, your workstation would contain two git repos, organized something like this:

```
/projects/
  - salt-bevy/
  - lessons/
```

As you learn to operate your testing bevy, your workstation file structure becomes like this:

```
/projects/
  - salt-bevy/
  - lessons/
  - black-knight/
 ```
 
 And finally, your working Salt Master controls several projects, and looks like:

 ```
/projects/
  - salt-bevy/
  - black-knight/
  - green-knight/
  - king-arthur/
```

### Installation

See the [detailed installation instructions here](lessons/installation/install.md). 

Then clone [salt-bevy](https://github.com/salt-bevy/salt-bevy.git)
and start [your lessons](lessons/index.md).
