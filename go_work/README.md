
# TBC (Tcl ByteCode) decoder

The .tbc file is generated by Tcl Pro. This repo try to add comments on .tbc file and disassemble .tbc file for human reading.  
test  .tbc file can be found [here](https://github.com/ActiveState/teapot/tree/master/lib/tbcload/tests/tbc10)

## Install

``` shell
go get github.com/corbamico/tbcload/tbcload
```

## Usage

``` shell
Usage:
  tbcload [command]

Available Commands:
  decode      encode a string into ascii85(re-map), which tbc file used
  decompile   disassemble a .tbc file, which can be on disk/url
  encode      A brief description of your command

Example:
    tbcload encode 123456
    tbcload encode  --hex "00010203"
    tbcload decompile test.tbc  #disassemble a file named test.tbc
    tbcload decompile --detail test.tbc
    tbcload decompile http://127.0.0.1/test.tcl #disassemble from a url

    example url, can be found as https://github.com/ActiveState/teapot/raw/master/lib/tbcload/tests/tbc10/proc.tbc
```

## Code Example

``` go
func ExampleEncode() {
    src := []byte("proc")
    dst := make([]byte, 150)
    length := Encode(dst, src)
    fmt.Printf("%s", dst[:length])
    // Output:
    // ,CHr@
}

func ExampleDecode() {
    r, _ := os.Open(uri)
    p := tbcload.NewParser(r, os.Stdout)
    p.Parse()
}

```

## Reference

- ActiveState Teapot [cmpWrite.c](https://github.com/ActiveState/teapot/blob/master/lib/tclcompiler/cmpWrite.c)

- ByteCode Definition Full Table [tclCompile.c](https://github.com/tcltk/tcl/blob/master/generic/tclCompile.c)


## License

- MIT

- ActiveState/teapot/cmpWrite.c BSD-3 license Copyright (c) 2017,ActiveState Software All rights reserved.
