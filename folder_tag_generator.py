import os,sys

if len(sys.argv) == 2:
    if sys.argv[1].lower() == 'true':
        file_dir = 'false'
        file_symbol = '^'
        print('symbol is: ^')
        filename_only = 'false'
        output_filename = 'output.txt'
    elif sys.argv[1].lower() != 'false':
        print('invalid arguments passed. argument must be either true or false')
        quit()

elif len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1].lower() == 'false'):
    print('File directory, type false for current directory')
    file_dir = input()
    print('Symbol to represent file name in tag line(Eg:&)')
    file_symbol = input()
    print('use filename only, type true for filename only, false to include file extention')
    filename_only = input()
    print('name for output file, false will default to output.txt')
    output_filename = input()
    if output_filename.lower() == 'false':
        output_filename = 'output.txt'

print('tag line with symbol in place for file names(Eg:<img src="$">)')
tag_line = input()
output = ''
if file_dir.lower() == 'false':
    files = os.listdir()
else:
    files = os.listdir(file_dir)

for f in files:
    if f == sys.argv[0] or not os.path.isfile(f):
        continue
    if filename_only.lower() == 'true':
        f = os.path.splitext(f)[0]
    new_tag = tag_line.replace(file_symbol,f)
    output += new_tag + '\n'

print(output)
f = open(output_filename, "w")
f.write(output)
f.close()

