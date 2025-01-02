local Tokenizer = require("tokenizer")

print("hello lua")
local buffer = "test volatile while 123"
local tokenizer = Tokenizer:init(buffer)
tokenizer:next()
