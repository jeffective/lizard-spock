local Token = require("token")

Tokenizer = {}
Tokenizer.__index = Tokenizer

---@return Tokenizer
---@param buffer string
function Tokenizer:init(buffer)
    ---@class Tokenizer
    local self = setmetatable({}, Tokenizer)
    self.buffer = buffer
    self.index = (buffer:sub(1, 3) == "\239\187\191") and 4 or 1
    return self
end

---@return Token|nil
function Tokenizer:next()
    ---@enum State
    local State = {
        start = 1,
        expect_newline = 2,
        identifier = 3,
        builtin = 4,
        string_literal = 5,
        string_literal_backslash = 6,
        multiline_string_literal_line = 7,
        char_literal = 8,
        char_literal_backslash = 9,
        backslash = 10,
        equal = 11,
        bang = 12,
        pipe = 13,
        minus = 14,
        minus_percent = 15,
        minus_pipe = 16,
        asterisk = 17,
        asterisk_percent = 18,
        asterisk_pipe = 19,
        slash = 20,
        line_comment_start = 21,
        line_comment = 22,
        doc_comment_start = 23,
        doc_comment = 24,
        int = 25,
        int_exponent = 26,
        int_period = 27,
        float = 28,
        float_exponent = 29,
        ampersand = 30,
        caret = 31,
        percent = 32,
        plus = 33,
        plus_percent = 34,
        plus_pipe = 35,
        angle_bracket_left = 36,
        angle_bracket_angle_bracket_left = 37,
        angle_bracket_angle_bracket_left_pipe = 38,
        angle_bracket_right = 39,
        angle_bracket_angle_bracket_right = 40,
        period = 41,
        period_2 = 42,
        period_asterisk = 43,
        saw_at_sign = 44,
        invalid = 45,
    }
    local token_value = ""
    local current_char = ""
    local state = State.start

    while true do
        current_char = self.buffer:sub(self.index, self.index)
        if state == State.start then
            if current_char == "\0" then
                if self.buffer.len() == self.index then
                    return Token:init(Token.Tag.eof, token_value)
                else
                    state = State.invalid
                end
            elseif current_char == ' ' or
                current_char == '\n' then
            end
        end
    end
    return nil
end

return Tokenizer
