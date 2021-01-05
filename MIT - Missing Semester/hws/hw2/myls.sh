myls () {

foo=$(ls -l -U)

for val in $foo; do
	if [[ $val = "\n" ]]; then
		echo "A"
	fi
done

}
