# File Manager 
This is a simple CLI tool to manipulate files in directories 

# Help 
```bash
$ python3 file_manager.py -h
```

# Commands
- Read a file 
```bash
$ python3 file_manager.py -r <file_name>
```

- Delete a file
```bash
$ python3 file_manager.py -d <file_name>
```

- Show files in a directory
```bash
$ python3 file_manager.py -s <directory_name>
```

- Copy content of file-1 to file-2
```bash
$ python3 file_manager.py -c <file1>    <file2>
```

- Rename old_filename to new_filename
```bash
$ python3 file_manager.py --rename <old_filename>   <new_filename>
```