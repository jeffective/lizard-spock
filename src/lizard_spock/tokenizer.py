
from enum import Enum, auto
from dataclasses import dataclass
import string

class Tag(Enum):
    invalid = auto()
    invalid_periodasterisks = auto()
    identifier = auto()
    string_literal = auto()
    multiline_string_literal_line =  auto()
    char_literal = auto()
    eof =  auto()
    builtin =  auto()
    bang = auto()
    pipe = auto()
    pipe_pipe = auto()
    pipe_equal = auto()
    equal = auto()
    equal_equal = auto()
    equal_angle_bracket_right = auto()
    bang_equal = auto()
    l_paren = auto()
    r_paren = auto()
    semicolon = auto()
    percent = auto()
    percent_equal = auto()
    l_brace = auto()
    r_brace = auto()
    l_bracket = auto()
    r_bracket = auto()
    period = auto()
    period_asterisk = auto()
    ellipsis2 = auto()
    ellipsis3 = auto()
    caret = auto()
    caret_equal = auto()
    plus = auto()
    plus_plus = auto()
    plus_equal = auto()
    plus_percent = auto()
    plus_percent_equal = auto()
    plus_pipe = auto()
    plus_pipe_equal = auto()
    minus = auto()
    minus_equal = auto()
    minus_percent = auto()
    minus_percent_equal = auto()
    minus_pipe = auto()
    minus_pipe_equal = auto()
    asterisk = auto()
    asterisk_equal = auto()
    asterisk_asterisk = auto()
    asterisk_percent = auto()
    asterisk_percent_equal = auto()
    asterisk_pipe = auto()
    asterisk_pipe_equal = auto()
    arrow = auto()
    colon = auto()
    slash = auto()
    slash_equal = auto()
    comma = auto()
    ampersand = auto()
    ampersand_equal = auto()
    question_mark = auto()
    angle_bracket_left = auto()
    angle_bracket_left_equal = auto()
    angle_bracket_angle_bracket_left = auto()
    angle_bracket_angle_bracket_left_equal = auto()
    angle_bracket_angle_bracket_left_pipe = auto()
    angle_bracket_angle_bracket_left_pipe_equal = auto()
    angle_bracket_right = auto()
    angle_bracket_right_equal = auto()
    angle_bracket_angle_bracket_right = auto()
    angle_bracket_angle_bracket_right_equal = auto()
    tilde = auto()
    number_literal = auto()
    doc_comment = auto()
    container_doc_comment = auto()
    keyword_addrspace = auto()
    keyword_align = auto()
    keyword_allowzero = auto()
    keyword_and = auto()
    keyword_anyframe = auto()
    keyword_anytype = auto()
    keyword_asm = auto()
    keyword_break = auto()
    keyword_callconv = auto()
    keyword_catch = auto()
    keyword_comptime = auto()
    keyword_const = auto()
    keyword_continue = auto()
    keyword_defer = auto()
    keyword_else = auto()
    keyword_enum = auto()
    keyword_errdefer = auto()
    keyword_error = auto()
    keyword_export = auto()
    keyword_extern = auto()
    keyword_fn = auto()
    keyword_for = auto()
    keyword_if = auto()
    keyword_inline = auto()
    keyword_noalias = auto()
    keyword_noinline = auto()
    keyword_nosuspend = auto()
    keyword_opaque = auto()
    keyword_or = auto()
    keyword_orelse = auto()
    keyword_packed = auto()
    keyword_pub = auto()
    keyword_resume = auto()
    keyword_return = auto()
    keyword_linksection = auto()
    keyword_struct = auto()
    keyword_suspend = auto()
    keyword_switch = auto()
    keyword_test = auto()
    keyword_threadlocal = auto()
    keyword_try = auto()
    keyword_union = auto()
    keyword_unreachable = auto()
    keyword_var = auto()
    keyword_volatile = auto()
    keyword_while = auto()

@dataclass
class Loc:
    start: int
    end: int

@dataclass
class Token:
    tag: Tag
    loc: Loc

def getKeyword(buffer: bytes) -> Tag | None:
    keywords = {
    b"addrspace": Tag.keyword_addrspace,
    b"align": Tag.keyword_align,
    b"allowzero": Tag.keyword_allowzero,
    b"and": Tag.keyword_and,
    b"anyframe": Tag.keyword_anyframe,
    b"anytype": Tag.keyword_anytype,
    b"asm": Tag.keyword_asm,
    b"break": Tag.keyword_break,
    b"callconv": Tag.keyword_callconv,
    b"catch": Tag.keyword_catch,
    b"comptime": Tag.keyword_comptime,
    b"const": Tag.keyword_const,
    b"continue": Tag.keyword_continue,
    b"defer": Tag.keyword_defer,
    b"else": Tag.keyword_else,
    b"enum": Tag.keyword_enum,
    b"errdefer": Tag.keyword_errdefer,
    b"error": Tag.keyword_error,
    b"export": Tag.keyword_export,
    b"extern": Tag.keyword_extern,
    b"fn": Tag.keyword_fn,
    b"for": Tag.keyword_for,
    b"if": Tag.keyword_if,
    b"inline": Tag.keyword_inline,
    b"noalias": Tag.keyword_noalias,
    b"noinline": Tag.keyword_noinline,
    b"nosuspend": Tag.keyword_nosuspend,
    b"opaque": Tag.keyword_opaque,
    b"or": Tag.keyword_or,
    b"orelse": Tag.keyword_orelse,
    b"packed": Tag.keyword_packed,
    b"pub": Tag.keyword_pub,
    b"resume": Tag.keyword_resume,
    b"return": Tag.keyword_return,
    b"linksection": Tag.keyword_linksection,
    b"struct": Tag.keyword_struct,
    b"suspend": Tag.keyword_suspend,
    b"switch": Tag.keyword_switch,
    b"test": Tag.keyword_test,
    b"threadlocal": Tag.keyword_threadlocal,
    b"try": Tag.keyword_try,
    b"union": Tag.keyword_union,
    b"unreachable": Tag.keyword_unreachable,
    b"var": Tag.keyword_var,
    b"volatile": Tag.keyword_volatile,
    b"while": Tag.keyword_while,
         }
    return keywords.get(buffer)


class State(Enum):
    start = auto()
    expect_newline = auto()
    identifier = auto()
    builtin = auto()
    string_literal = auto()
    string_literal_backslash = auto()
    multiline_string_literal_line = auto()
    char_literal = auto()
    char_literal_backslash = auto()
    backslash = auto()
    equal = auto()
    bang = auto()
    pipe = auto()
    minus = auto()
    minus_percent = auto()
    minus_pipe = auto()
    asterisk = auto()
    asterisk_percent = auto()
    asterisk_pipe = auto()
    slash = auto()
    line_comment_start = auto()
    line_comment = auto()
    doc_comment_start = auto()
    doc_comment = auto()
    int = auto()
    int_exponent = auto()
    int_period = auto()
    float = auto()
    float_exponent = auto()
    ampersand = auto()
    caret = auto()
    percent = auto()
    plus = auto()
    plus_percent = auto()
    plus_pipe = auto()
    angle_bracket_left = auto()
    angle_bracket_angle_bracket_left = auto()
    angle_bracket_angle_bracket_left_pipe = auto()
    angle_bracket_right = auto()
    angle_bracket_angle_bracket_right = auto()
    period = auto()
    period_2 = auto()
    period_asterisk = auto()
    saw_at_sign = auto()
    invalid = auto()

string_literal_thing = set([x for x in range(0x01, 0x09)] + [x for x in range(0x0b, 0x1f)] + [0x7f] )

class Tokenizer:

    def __init__(self, buffer: bytes):
        self.index = 0
        self.buffer = buffer
    
    def next(self) -> Token:
        state = State.start
        result = Token(Tag.eof, Loc(self.index, self.index))
        while (True):
            match state:
                case State.start:
                    match self.buffer[self.index]:
                        case 0:
                            if self.index == len(self.buffer):
                                return Token(Tag.eof, Loc(self.index, self.index))
                            else:
                                state = State.invalid
                                continue
                        case ' ', '\n', '\t', '\r':
                            self.index += 1
                            result.loc.start = self.index
                            state = State.start
                            continue
                        case '"':
                            result.tag = Tag.string_literal
                            state = State.string_literal
                            continue
                        case '\'':
                            result.tag = Tag.char_literal
                            state = State.char_literal
                            continue
                        case string.ascii_letters | '_':
                            result.tag = Tag.identifier
                            state = State.identifier
                            continue
                        case '@':
                            state = State.saw_at_sign
                            continue
                        case '=':
                            state = State.equal
                            continue
                        case '!':
                            state = State.bang
                            continue
                        case '|':
                            state = State.pipe
                            continue
                        case '(':
                            result.tag = Tag.l_paren
                            self.index += 1
                        case ')':
                            result.tag = Tag.r_paren
                            self.index += 1
                        case '[':
                            result.tag = Tag.l_bracket
                            self.index += 1
                        case ']':
                            result.tag = Tag.r_bracket
                            self.index += 1
                        case ';':
                            result.tag = Tag.semicolon
                            self.index += 1
                        case ',':
                            result.tag = Tag.comma
                            self.index += 1
                        case '?':
                            result.tag = Tag.question_mark
                            self.index += 1
                        case ':':
                            result.tag = Tag.colon
                            self.index += 1
                        case '%':
                            state = State.percent
                            continue
                        case '*':
                            state = State.asterisk
                            continue
                        case '+':
                            state = State.plus
                            continue
                        case '<':
                            state = State.angle_bracket_left
                            continue
                        case '>':
                            state = State.angle_bracket_right
                            continue
                        case '^':
                            state = State.caret
                            continue
                        case '\\':
                            result.tag = Tag.multiline_string_literal_line
                            state = State.backslash
                            continue
                        case '{':
                            result.tag = Tag.l_brace
                            self.index += 1
                        case '}':
                            result.tag = Tag.r_brace
                            self.index += 1
                        case '~':
                            result.tag = Tag.tilde
                            self.index += 1
                        case '.':
                            state = State.period
                            continue
                        case '-':
                            state = State.minus
                            continue
                        case '/':
                            state = State.slash
                            continue
                        case '&':
                            state = State.ampersand
                            continue
                        case string.digits:
                            result.tag = Tag.number_literal
                            self.index += 1
                            state = State.int
                            continue
                        case _:
                            state = State.invalid
                            continue
                case State.expect_newline:
                    self.index += 1
                    match self.buffer[self.index]:
                        case 0:
                            if self.index == len(self.buffer):
                                result.tag = Tag.invalid
                            else:
                                state = State.invalid
                                continue
                        case '\n':
                            self.index += 1
                            result.loc.start = self.index
                            state = State.start
                            continue
                        case _:
                            state = State.invalid
                            continue
                case State.invalid:
                    self.index += 1
                    match self.buffer[self.index]:
                        case 0:
                            if self.index == len(self.buffer):
                                result.tag = Tag.invalid
                            else:
                                state = State.invalid
                                continue
                        case '\n':
                            result.tag = Tag.invalid
                        case _:
                            state = State.invalid
                            continue
                case State.saw_at_sign:
                    self.index += 1
                    match self.buffer[self.index]:
                        case 0, '\n':
                            result.tag = Tag.invalid
                        case '"':
                            result.tag = Tag.identifier
                            state = State.string_literal
                            continue
                        case string.ascii_letters | '_':
                            result.tag = Tag.builtin
                            state = State.builtin
                            continue
                        case _:
                            state = State.invalid
                            continue
                case State.ampersand:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.ampersand_equal
                            self.index += 1
                        case _:
                            result.tag = Tag.ampersand
                case State.asterisk:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.asterisk_equal
                            self.index += 1
                        case '*':
                            result.tag = Tag.asterisk_asterisk
                            self.index += 1
                        case '%':
                            state = State.asterisk_percent
                            continue
                        case '|':
                            state = State.asterisk_pipe
                        case _:
                            result.tag = Tag.asterisk
                case State.asterisk_percent:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.asterisk_percent_equal
                            self.index += 1
                        case _:
                            result.tag = Tag.asterisk_percent
                case State.asterisk_pipe:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.asterisk_pipe_equal
                            self.index += 1
                        case _:
                            result.tag = Tag.asterisk_pipe
                case State.percent:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.percent_equal
                            self.index += 1
                        case _:
                            result.tag = Tag.percent
                case State.plus:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.plus_equal
                            self.index += 1
                        case '+':
                            result.tag = Tag.plus_plus
                            self.index += 1
                        case '%':
                            state = State.plus_percent
                            continue
                        case '|':
                            state = State.plus_pipe
                            continue
                        case _:
                            result.tag = Tag.plus
                ########################################
                case State.plus_percent:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.plus_percent_equal
                            self.index += 1
                        case _:
                            result.tag = Tag.plus_percent
                case State.plus_pipe:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.plus_equal
                            self.index += 1
                        case _:
                            result.tag = Tag.plus_pipe
                        
                    
                case State.caret:
                    self.index += 1
                    match self.buffer[self.index]:
                        case '=':
                            result.tag = Tag.caret_equal
                            self.index =+1 
                        case _:
                            result.tag = Tag.caret

                    
                case State.identifier:
                    self.index += 1
                    match self.buffer[self.index]:
                        case string.ascii_letters | string.digits | '_':
                            state = State.identifier
                            continue
                        case _:
                            ident = self.buffer[result.loc.start:self.index]
                            if tag := getKeyword(ident):
                                result.tag = tag
                    
                case State.builtin:
                    self.index += 1
                    match self.buffer[self.index]:
                        case string.ascii_letters | string.digits | '_':
                            state = State.builtin
                        case _:
                            pass
                    
                case State.backslash:
                    self.index += 1
                    match self.buffer[self.index]:
                        case 0:
                            result.tag = Tag.invalid
                        case '\\':
                            state = State.multiline_string_literal_line
                            continue
                        case '\n':
                            result.tag = State.invalid
                        case _:
                            state = State.invalid
                            continue

                case State.string_literal:
                    self.index += 1
                    match self.buffer[self.index]:
                        case 0:
                            if self.index != len(self.buffer):
                                state = State.invalid
                                continue
                            else:
                                result.tag = Tag.invalid
                        case '\n':
                            result.tag = Tag.invalid
                        case '\\':
                            state = State.string_literal_backslash
                            continue
                        case '"':
                            self.index += 1
                        case string_literal_thing:
                            state = State.invalid
                            continue
                        case _:
                            state = State.string_literal
                            continue

                    
                case State.string_literal_backslash:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.char_literal:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.char_literal_backslash:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.multiline_string_literal_line:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.bang:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.pipe:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.equal:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.minus:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.minus_percent:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.minus_pipe:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.angle_bracket_left:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.angle_bracket_angle_bracket_left:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.angle_bracket_angle_bracket_left_pipe:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.angle_bracket_right:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.angle_bracket_angle_bracket_right:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.period:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.period_2:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.period_asterisk:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.slash:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.line_comment_start:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.doc_comment_start:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.line_comment:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.doc_comment:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.int:
                    match self.buffer[self.index]:
                    
                case State.int_exponent:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.int_period:
                    self.index += 1
                    match self.buffer[self.index]:
                    
                case State.float:
                    match self.buffer[self.index]:
                    
                case State.float_exponent:
                    self.index += 1
                    match self.buffer[self.index]:
                    
            break
        result.loc.end = self.index
        return result



                            
                            



