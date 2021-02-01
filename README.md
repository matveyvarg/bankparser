# bankparser
Parser for bank files


## Usage
To run app create new instance of App class:
```
app = App(fieldmaps, reader_class, writer_class)
```

**Arguments**:

`filedmaps`: `list of files in following format:
(_path to file_, {_field_to_map_: _field_map_from_})

In case of date field, specify date format
1. If you have the same name in csv field:
`(path_to_file, {date_field: format})`
You can look for format here 
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
2. If the name of field is different:
`(path_to_file, {date_field: (fieldname: format)})`

In case you don't want to specify field map use `None` insted:
```
(path_to_file, None)
```
