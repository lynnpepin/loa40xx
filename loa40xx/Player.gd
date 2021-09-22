extends KinematicBody2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var  SPEED = 256
var DIRECTION = Vector2(0,0)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func _process(delta):
	pass
	
func _physics_process(delta):
	DIRECTION.x = (int(Input.is_action_pressed("pad_right")) - int(Input.is_action_pressed("pad_left")))
	DIRECTION.y = (int(Input.is_action_pressed("pad_down")) - int(Input.is_action_pressed("pad_up")))
	move_and_slide(DIRECTION.normalized()*SPEED)



# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
