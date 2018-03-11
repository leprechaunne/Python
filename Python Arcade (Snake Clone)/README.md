# Python
## Synopsis

This is a simple demonstration of an OOP program of snake using a graphics API by John Zelle
It's primary purpose is to demonstrate creating a program from scratch with proper syntax


## Changelog


-- 3# for major change (Alpha to Beta, 1.8 to 2.0, etc)
-- 4# for @--#.X change (aka A--1.1 to A--1.2)
-- 5# for @--#.#.X (minor changes like A--5.3.1 usually for hotfixes)

#### A--2.1
Added snake spawning with option color
KNOWN ISSUES: endless loop, doesn't fully clear screen, one weird pixel persists, border not drawn

### A--2.0
Complete structure overhaul! Now that it has its own branch in the main repository, I took
to cleaning up the code and organizing the functions and classes so it's easier to edit.

As such, some previously functioning features are not yet implemented, so the todo will change with
this upload.

#### A--1.8
Doesn't crash anymore
Apple spawns inside borders only (snake still not bound)

#### A--1.7
Apple spawns somewhere not occupied by snake

#### A--1.6
Disabled 180 degree movement (pretty easy, given its only one condition for 4 directions)

##### A--1.5
Fixed the snake 'jumping'... i was skipping a full grid space instead of going to the next

##### A--1.4
Changed subtitle text and the key to exit title screen to Enter (so difficulty can be added later)
Tweaked tick to be a little faster
Snake can be controled AND maintains the length

#### A--1.3 
Fixed direction confusion (got my x and y backwords) (and the y sign (+/-))
Fixed tick function by swapping getKey() with checkKey()

##### A--1.2 
Made snake move on button press

##### A--1.1 
Added boundary and key reading command and tick, but no action on tick yet

##### A--1.0 
Drew a Window and a Square (impressive, I know)

## TOREDO
### Snake moving
### Apple Spawning
### Snake growing (although this one was never fully implemented yet)

## TODO (SOON)
### 'Apple' eating
### Restrict movement OoB -- This one I've sort of done... I structured the new grid->coords method to handle it
### EDIT: snake& size increase

##TODO (EVENTUALLY)

### Add difficulty
### Add Score tracking
### Add high scores
### Add visible timer
### Dynamic timer to speed up TICKS ONLY, the visible timer is for player reference

