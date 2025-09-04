import file_operations

context = {
	"first_name": "Sarah",
	"last_name": "Connor"
}

file_operations.render_template("src/charsheet.svg", "result.svg", context)
file_operations.render_template("src/charsheet.svg", "output/result.svg", context)

