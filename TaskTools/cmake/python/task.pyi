# PyWaamAPI.pyi (Corrected based on C++ and SWIG files with Pythonic Docstrings)
from typing import Any, Callable, Dict, Generic, Iterable, Iterator, List, Optional, Tuple, Type, TypeVar, Union, overload, Sequence, Mapping
from collections.abc import MutableSequence, MutableMapping

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

FRAME_TOOL: int
FRAME_BASE: int
FRAME_USER1: int
FRAME_USER2: int
FRAME_USER3: int
FRAME_USER4: int
FRAME_USER5: int
FRAME_USER6: int
FRAME_USER7: int
FRAME_USER8: int
FRAME_USER9: int
FRAME_USER10: int
FRAME_USER11: int
FRAME_USER12: int
FRAME_USER13: int
FRAME_USER14: int
FRAME_USER15: int
FRAME_USER16: int
FRAME_USER17: int
FRAME_USER18: int
TOOL_0: int
TOOL_1: int
TOOL_2: int
TOOL_3: int
TOOL_4: int
TOOL_5: int
TOOL_6: int
TOOL_7: int
TOOL_8: int
TOOL_9: int
TOOL_10: int
TOOL_11: int
TOOL_12: int
TOOL_13: int
TOOL_14: int
TOOL_15: int
TOOL_16: int
TOOL_17: int
TOOL_18: int
TOOL_19: int

# This class is a placeholder for the SWIG-generated low-level module.
# In a real scenario, if _PyWaamAPI.pyi exists, it would be used.
# For now, we make attributes Any or specific if known.
class _PyWaamAPI:
    """Low-level SWIG-generated module (placeholder).

    This class is a stub for the internal module created by SWIG.
    In a real scenario, definitions imported from the compiled C++ code would be here.
    """
    class cvar:
        """Contains constants and global variables from C++, exported by SWIG.

        For example, formatting flags for iostream or global objects like cin/cout.
        """
        ios_base_boolalpha: int
        ios_base_dec: int
        ios_base_fixed: int
        ios_base_hex: int
        ios_base_internal: int
        ios_base_left: int
        ios_base_oct: int
        ios_base_right: int
        ios_base_scientific: int
        ios_base_showbase: int
        ios_base_showpoint: int
        ios_base_showpos: int
        ios_base_skipws: int
        ios_base_unitbuf: int
        ios_base_uppercase: int
        ios_base_adjustfield: int
        ios_base_basefield: int
        ios_base_floatfield: int
        ios_base_badbit: int
        ios_base_eofbit: int
        ios_base_failbit: int
        ios_base_goodbit: int
        ios_base_app: int
        ios_base_ate: int
        ios_base_binary: int
        ios_base_ios_base_in: int # Renamed from 'in'
        ios_base_out: int
        ios_base_trunc: int
        ios_base_beg: int
        ios_base_cur: int
        ios_base_end: int
        cin: "istream"
        cout: "ostream"
        cerr: "ostream"
        clog: "ostream"
    # Add stubs for other functions/classes from _PyWaamAPI if directly used
    # For brevity, we'll assume types are handled by the wrapper classes.

# Helper functions and classes (usually internal SWIG machinery)
def _swig_repr(self: Any) -> str:
    """SWIG helper function to generate a string representation of an object."""
    ...
def _swig_setattr_nondynamic_instance_variable(set_func: Callable[[Any, str, Any], None]) -> Callable[[Any, str, Any], None]:
    """SWIG helper function to set instance attributes (non-dynamic)."""
    ...
def _swig_setattr_nondynamic_class_variable(set_func: Callable[[Type[Any], str, Any], None]) -> Callable[[Type[Any], str, Any], None]:
    """SWIG helper function to set class attributes (non-dynamic)."""
    ...
def _swig_add_metaclass(metaclass: Type[Any]) -> Callable[[Type[Any]], Type[Any]]:
    """SWIG helper function to add a metaclass."""
    ...

class _SwigNonDynamicMeta(type):
    """SWIG metaclass to prevent dynamic addition of attributes."""
    def __setattr__(cls, name: str, value: Any) -> None: ...

class SwigPyIterator(Iterator[_T]):
    """SWIG iterator wrapping C++ iterators.

    Provides a standard Python iterator interface.
    """
    thisown: property
    def __init__(self, *args: Any, **kwargs: Any) -> None: ... # Abstract
    def __swig_destroy__(self) -> None:
        """SWIG-managed destructor."""
        ...
    def value(self) -> _T:
        """Returns the current value pointed to by the iterator.

        Returns:
            _T: The current element.
        """
        ...
    def incr(self, n: int = 1) -> "SwigPyIterator[_T]":
        """Advances the iterator by n positions.

        Args:
            n (int, optional): The number of positions to advance. Defaults to 1.

        Returns:
            SwigPyIterator[_T]: The iterator itself after advancing.
        """
        ...
    def decr(self, n: int = 1) -> "SwigPyIterator[_T]":
        """Moves the iterator backward by n positions.

        Args:
            n (int, optional): The number of positions to move back. Defaults to 1.

        Returns:
            SwigPyIterator[_T]: The iterator itself after moving.
        """
        ...
    def distance(self, x: "SwigPyIterator[_T]") -> int:
        """Calculates the distance to another iterator.

        Args:
            x (SwigPyIterator[_T]): Another iterator.

        Returns:
            int: The distance between this iterator and x.
        """
        ...
    def equal(self, x: "SwigPyIterator[_T]") -> bool:
        """Checks if this iterator is equal to another iterator.

        Args:
            x (SwigPyIterator[_T]): Another iterator.

        Returns:
            bool: True if the iterators are equal, False otherwise.
        """
        ...
    def copy(self) -> "SwigPyIterator[_T]":
        """Creates a copy of this iterator.

        Returns:
            SwigPyIterator[_T]: A new SwigPyIterator instance.
        """
        ...
    def next(self) -> _T:
        """Advances the iterator and returns the next value.

        Note:
            For Python 2 compatibility. In Python 3, `__next__` is preferred.

        Returns:
            _T: The next element.
        """
        ...
    def __next__(self) -> _T:
        """Advances the iterator and returns the next value.

        Returns:
            _T: The next element.
        """
        ...
    def previous(self) -> _T:
        """Moves the iterator to the previous value and returns it.

        Returns:
            _T: The previous element.
        """
        ...
    def advance(self, n: int) -> "SwigPyIterator[_T]":
        """Advances the iterator by a specific number of steps.

        Args:
            n (int): The number of steps to advance. Can be negative to move backward.

        Returns:
            SwigPyIterator[_T]: The iterator itself after advancing.
        """
        ...
    def __eq__(self, x: Any) -> bool:
        """Equality comparison.

        Args:
            x (Any): Object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        ...
    def __ne__(self, x: Any) -> bool:
        """Inequality comparison.

        Args:
            x (Any): Object to compare with.

        Returns:
            bool: True if not equal, False otherwise.
        """
        ...
    def __iadd__(self, n: int) -> "SwigPyIterator[_T]":
        """In-place addition (advances iterator).

        Args:
            n (int): Number of steps to advance.

        Returns:
            SwigPyIterator[_T]: The iterator itself.
        """
        ...
    def __isub__(self, n: int) -> "SwigPyIterator[_T]":
        """In-place subtraction (moves iterator backward).

        Args:
            n (int): Number of steps to move backward.

        Returns:
            SwigPyIterator[_T]: The iterator itself.
        """
        ...
    def __add__(self, n: int) -> "SwigPyIterator[_T]":
        """Addition (returns a new advanced iterator).

        Args:
            n (int): Number of steps to advance.

        Returns:
            SwigPyIterator[_T]: A new iterator advanced by n steps.
        """
        ...
    @overload
    def __sub__(self, n: int) -> "SwigPyIterator[_T]": ...
    @overload
    def __sub__(self, x: "SwigPyIterator[_T]") -> int: ...
    def __sub__(self, *args: Any) -> Any:
        """Subtraction.

        If an int is provided, returns a new iterator moved backward.
        If another SwigPyIterator is provided, returns the distance.
        """
        ... # Implementation for overload
    def __iter__(self) -> "SwigPyIterator[_T]":
        """Returns the iterator itself (required for iterator protocol).

        Returns:
            SwigPyIterator[_T]: The iterator itself.
        """
        ...

# Standard C++ iostream classes (if exposed by SWIG's std_iostream.i)
class ios_base:
    """Base class for stream I/O.

    Provides formatting and error state facilities for stream classes.
    """
    thisown: property
    erase_event: int; imbue_event: int; copyfmt_event: int
    # Flags (constants are accessed via cvar in the actual Python module)
    boolalpha: int; dec: int; fixed: int; hex: int; internal: int; left: int; oct: int
    right: int; scientific: int; showbase: int; showpoint: int; showpos: int
    skipws: int; unitbuf: int; uppercase: int; adjustfield: int; basefield: int
    floatfield: int; badbit: int; eofbit: int; failbit: int; goodbit: int
    app: int; ate: int; binary: int; ios_base_in: int; out: int; trunc: int
    beg: int; cur: int; end: int
    def __init__(self, *args: Any, **kwargs: Any) -> None: ... # Typically no public constructor
    def __repr__(self) -> str: ...
    def register_callback(self, fn: Callable[[int, "ios_base", int], None], index: int) -> None:
        """Registers a callback function.

        Args:
            fn (Callable[[int, "ios_base", int], None]): The callback function.
            index (int): An integer index for the callback.
        """
        ...
    def flags(self, fmtfl: Optional[int] = None) -> int:
        """Gets or sets format flags.

        Args:
            fmtfl (Optional[int]): New format flags to set.

        Returns:
            int: The current (or previous) format flags.
        """
        ...
    def setf(self, fmtfl: int, mask: Optional[int] = None) -> int:
        """Sets specified format flags.

        Args:
            fmtfl (int): Format flags to set.
            mask (Optional[int]): Mask specifying which flags to alter.

        Returns:
            int: The previous format flags.
        """
        ...
    def unsetf(self, mask: int) -> None:
        """Clears specified format flags.

        Args:
            mask (int): Mask specifying which flags to clear.
        """
        ...
    def precision(self, prec: Optional[int] = None) -> int:
        """Gets or sets the floating-point precision.

        Args:
            prec (Optional[int]): New precision to set.

        Returns:
            int: The current (or previous) precision.
        """
        ...
    def width(self, wide: Optional[int] = None) -> int:
        """Gets or sets the field width.

        Args:
            wide (Optional[int]): New field width to set.

        Returns:
            int: The current (or previous) field width.
        """
        ...
    @staticmethod
    def sync_with_stdio(sync: bool = True) -> bool:
        """Synchronizes C++ streams with C standard streams.

        Args:
            sync (bool): Whether to synchronize. Defaults to True.

        Returns:
            bool: The previous synchronization state.
        """
        ...
    def imbue(self, loc: Any) -> Any: # locale
        """Sets or gets the current locale.

        Args:
            loc (Any): The locale object to set.

        Returns:
            Any: The previous locale.
        """
        ...
    def getloc(self) -> Any: # locale
        """Gets the current locale.

        Returns:
            Any: The current locale object.
        """
        ...
    @staticmethod
    def xalloc() -> int:
        """Allocates a new, unused stream storage index.

        Returns:
            int: A unique integer index.
        """
        ...
    def iword(self, ix: int) -> int: # long&
        """Accesses a user-defined integer storage location.

        Args:
            ix (int): The index obtained from xalloc().

        Returns:
            int: A reference to the integer storage.
        """
        ...
    def pword(self, ix: int) -> Any: # void*&
        """Accesses a user-defined pointer storage location.

        Args:
            ix (int): The index obtained from xalloc().

        Returns:
            Any: A reference to the pointer storage.
        """
        ...
    def __swig_destroy__(self) -> None:
        """SWIG-managed destructor."""
        ...

cvar: _PyWaamAPI.cvar # Expose cvar from the low-level module

class ios(ios_base):
    """Base class for input/output streams.

    Inherits formatting and error state from ios_base and adds stream buffer management.
    """
    def __init__(self, sb: Any) -> None: # streambuf*
        """Constructor.

        Args:
            sb (Any): Pointer to a stream buffer.
        """
        ...
    def rdstate(self) -> int:
        """Returns the current stream error state flags.

        Returns:
            int: The error state flags (e.g., goodbit, eofbit, failbit, badbit).
        """
        ...
    def clear(self, state: int = 0) -> None: # Default is goodbit (0)
        """Sets the stream error state flags.

        Args:
            state (int): The new error state flags. Defaults to goodbit (no errors).
        """
        ...
    def setstate(self, state: int) -> None:
        """Adds specified flags to the current stream error state.

        Args:
            state (int): Flags to add (e.g., failbit).
        """
        ...
    def good(self) -> bool:
        """Checks if the stream is in a good state (no errors).

        Returns:
            bool: True if no error flags are set, False otherwise.
        """
        ...
    def eof(self) -> bool:
        """Checks if the stream has reached end-of-file.

        Returns:
            bool: True if eofbit is set, False otherwise.
        """
        ...
    def fail(self) -> bool:
        """Checks if a logical error occurred on the stream (failbit or badbit is set).

        Returns:
            bool: True if failbit or badbit is set, False otherwise.
        """
        ...
    def bad(self) -> bool:
        """Checks if a severe I/O error occurred on the stream (badbit is set).

        Returns:
            bool: True if badbit is set, False otherwise.
        """
        ...
    def exceptions(self, except_mask: Optional[int] = None) -> int:
        """Gets or sets the exception mask.

        Specifies which stream state flags will cause an exception to be thrown.

        Args:
            except_mask (Optional[int]): New exception mask to set.

        Returns:
            int: The current (or previous) exception mask.
        """
        ...
    def tie(self, tiestr: Optional["ostream"] = None) -> Optional["ostream"]:
        """Gets or sets the tied output stream.

        The tied stream is flushed before each input/output operation on this stream.

        Args:
            tiestr (Optional["ostream"]): The output stream to tie to this stream. Pass None to untie.

        Returns:
            Optional["ostream"]: The previously tied output stream, or None if no stream was tied.
        """
        ...
    def rdbuf(self, sb: Optional[Any] = None) -> Any: # streambuf*
        """Gets or sets the associated stream buffer.

        Args:
            sb (Optional[Any]): A new stream buffer to associate with this stream.

        Returns:
            Any: A pointer to the current (or previous) stream buffer.
        """
        ...
    def copyfmt(self, rhs: "ios") -> "ios":
        """Copies all formatting information from another ios object.

        Args:
            rhs ("ios"): The ios object to copy formatting from.

        Returns:
            "ios": *this
        """
        ...
    def fill(self, ch: Optional[str] = None) -> str:
        """Gets or sets the fill character.

        The fill character is used to pad output to the field width.

        Args:
            ch (Optional[str]): The new fill character to set. Must be a single character string.

        Returns:
            str: The current (or previous) fill character.
        """
        ...
    # imbue, narrow, widen would also be here if specialized

class ostream(ios):
    """Output stream class.

    Provides methods for formatted and unformatted output.
    """
    def __init__(self, sb: Any) -> None: # streambuf*
        """Constructor.

        Args:
            sb (Any): Pointer to a stream buffer.
        """
        ...
    def __lshift__(self, val: Any) -> "ostream": # Covers all operator<< overloads
        """Inserts formatted data into the stream.

        This is the Python equivalent of C++ operator<<.

        Args:
            val (Any): The value to insert.

        Returns:
            "ostream": *this
        """
        ...
    def put(self, c: str) -> "ostream":
        """Inserts a single character into the stream.

        Args:
            c (str): The character to insert. Must be a single character string.

        Returns:
            "ostream": *this
        """
        ...
    def write(self, s: Union[str, bytes], n: int) -> "ostream":
        """Inserts a block of characters into the stream.

        Args:
            s (Union[str, bytes]): The string or bytes containing characters to insert.
            n (int): The number of characters to write.

        Returns:
            "ostream": *this
        """
        ...
    def flush(self) -> "ostream":
        """Flushes the output stream.

        Synchronizes the associated stream buffer with its external destination.

        Returns:
            "ostream": *this
        """
        ...
    def tellp(self) -> int: # pos_type
        """Returns the current output position indicator.

        Returns:
            int: The current position in the output sequence.
        """
        ...
    def seekp(self, pos_or_off: int, dir: Optional[int] = None) -> "ostream": # dir is seekdir
        """Sets the current output position indicator.

        Args:
            pos_or_off (int): Either an absolute position or an offset.
            dir (Optional[int]): The direction for offset (e.g., ios_base.beg, ios_base.cur, ios_base.end).
                                 Required if pos_or_off is an offset.

        Returns:
            "ostream": *this
        """
        ...

class istream(ios):
    """Input stream class.

    Provides methods for formatted and unformatted input.
    """
    def __init__(self, sb: Any) -> None: # streambuf*
        """Constructor.

        Args:
            sb (Any): Pointer to a stream buffer.
        """
        ...
    def __rshift__(self, val: Any) -> "istream": # Covers all operator>> overloads
        """Extracts formatted data from the stream.

        This is the Python equivalent of C++ operator>>.
        The actual type of 'val' will depend on how SWIG wraps the C++ overloads
        (e.g., it might expect a mutable type like a list to store the extracted value).

        Args:
            val (Any): A variable to store the extracted data.

        Returns:
            "istream": *this
        """
        ...
    def gcount(self) -> int: # streamsize
        """Returns the number of characters extracted by the last unformatted input operation.

        Returns:
            int: The number of characters extracted.
        """
        ...
    def get(self, *args: Any) -> Any:
        """Extracts characters from the stream.

        This method has multiple overloads in C++. The Python signature might vary.
        Common forms:
        - get(): Extracts a single character and returns its integer value.
        - get(char_ref): Extracts a single character and stores it.
        - get(char_ptr, count, delim): Extracts a C-string.

        Args:
            args: Arguments for the specific overload.

        Returns:
            Any: Depends on the overload (e.g., int, or the stream itself).
        """
        ...
    def getline(self, s_list: List[str], n: int, delim: Optional[str] = None) -> "istream":
        """Extracts a line of characters from the stream.

        Reads characters until n-1 characters are read, the delimiter is found, or EOF is reached.

        Args:
            s_list (List[str]): A list (acting as a buffer) to store the extracted C-string.
                                Typically `s_list[0]` will hold the string.
            n (int): The maximum number of characters to write to s_list (including null terminator).
            delim (Optional[str]): The delimiter character. Defaults to newline.

        Returns:
            "istream": *this
        """
        ...
    def ignore(self, n: int = 1, delim: int = -1) -> "istream": # delim is traits::eof()
        """Extracts and discards characters from the stream.

        Args:
            n (int): The maximum number of characters to extract. Defaults to 1.
            delim (int): A delimiter character. Extraction stops if this character is found.
                         Defaults to EOF (-1 typically represents traits::eof()).

        Returns:
            "istream": *this
        """
        ...
    def peek(self) -> int: # int_type
        """Returns the next character in the stream without extracting it.

        Returns:
            int: The integer value of the next character, or EOF if at end-of-file.
        """
        ...
    def read(self, s_list: List[str], n: int) -> "istream":
        """Extracts a block of characters from the stream.

        Args:
            s_list (List[str]): A list (acting as a buffer) to store the extracted characters.
                                `s_list[0]` will hold the data.
            n (int): The number of characters to read.

        Returns:
            "istream": *this
        """
        ...
    def readsome(self, s_list: List[str], n: int) -> int: # streamsize
        """Extracts available characters from the stream buffer.

        Reads at most n characters. Does not wait for more characters if the buffer is not full.

        Args:
            s_list (List[str]): A list (acting as a buffer) to store the extracted characters.
                                `s_list[0]` will hold the data.
            n (int): The maximum number of characters to read.

        Returns:
            int: The number of characters actually read.
        """
        ...
    def putback(self, c: str) -> "istream":
        """Puts a character back into the stream.

        The next input operation will read this character first.

        Args:
            c (str): The character to put back. Must be a single character string.

        Returns:
            "istream": *this
        """
        ...
    def unget(self) -> "istream":
        """Moves the stream's get pointer one character backward.

        Allows the last read character to be read again.

        Returns:
            "istream": *this
        """
        ...
    def sync(self) -> int:
        """Synchronizes the stream buffer with the source of characters.

        Returns:
            int: 0 on success, -1 on failure.
        """
        ...
    def tellg(self) -> int: # pos_type
        """Returns the current input position indicator.

        Returns:
            int: The current position in the input sequence.
        """
        ...
    def seekg(self, pos_or_off: int, dir: Optional[int] = None) -> "istream": # dir is seekdir
        """Sets the current input position indicator.

        Args:
            pos_or_off (int): Either an absolute position or an offset.
            dir (Optional[int]): The direction for offset (e.g., ios_base.beg, ios_base.cur, ios_base.end).
                                 Required if pos_or_off is an offset.

        Returns:
            "istream": *this
        """
        ...

class iostream(istream, ostream):
    """Input/output stream class.

    Combines functionality of istream and ostream.
    """
    def __init__(self, sb: Any) -> None: # streambuf*
        """Constructor.

        Args:
            sb (Any): Pointer to a stream buffer.
        """
        ...

# Global iostream objects (from cvar)
cin: istream
cout: ostream
cerr: ostream
clog: ostream
# Manipulators - their exact types are function pointers or objects behaving like them
endl: Any
ends: Any
flush: Any
SHARED_PTR_DISOWN: int

# SWIG-generated template specializations for std::vector
class StringVector(MutableSequence[str]):
    """SWIG wrapper for std::vector<std::string>.

    Provides a Pythonic interface to a C++ vector of strings.
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[str]) -> None: ...
    @overload
    def __init__(self, other: "StringVector") -> None: ... # Copy constructor
    def __init__(self, *args: Any) -> None:
        """Constructor for StringVector.

        Can be initialized empty, with a size, from an iterable, or by copying another StringVector.

        Examples:
        ```python
        v1 = StringVector()
        v2 = StringVector(5)
        v3 = StringVector(["hello", "world"])
        v4 = StringVector(v3)
        ```
        """
        ...

    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> str: ...
    @overload
    def __getitem__(self, slice_obj: slice) -> "StringVector": ...
    def __getitem__(self, key: Union[int, slice]) -> Union[str, "StringVector"]: ...
    @overload
    def __setitem__(self, index: int, value: str) -> None: ...
    @overload
    def __setitem__(self, slice_obj: slice, value: Iterable[str]) -> None: ...
    def __setitem__(self, key: Union[int, slice], value: Any) -> None: ...
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def append(self, x: str) -> None:
        """Appends an element to the end of the vector.

        Args:
            x (str): The string to append.
        """
        ...
    def pop(self, index: Optional[int] = None) -> str:
        """Removes and returns an element at the given index (default last).

        Args:
            index (Optional[int]): The index of the element to pop. Defaults to the last element.

        Returns:
            str: The removed string.
        """
        ...
    def clear(self) -> None:
        """Removes all elements from the vector."""
        ...
    def extend(self, iterable: Iterable[str]) -> None:
        """Extends the vector by appending elements from an iterable.

        Args:
            iterable (Iterable[str]): An iterable of strings.
        """
        ...
    def insert(self, index: int, value: str) -> None:
        """Inserts an element at a given position.

        Args:
            index (int): The index at which to insert.
            value (str): The string to insert.
        """
        ...
    def push_back(self, x: str) -> None:
        """Appends an element to the end of the vector (C++ style).

        Args:
            x (str): The string to append.
        """
        ...
    def pop_back(self) -> None: # In C++ std::vector::pop_back is void
        """Removes the last element from the vector (C++ style).

        Note:
            SWIG might map this to return the popped element or be void.
            The provided .pyi suggests void, matching C++.
        """
        ...
    def empty(self) -> bool:
        """Checks if the vector is empty.

        Returns:
            bool: True if the vector is empty, False otherwise.
        """
        ...
    def size(self) -> int:
        """Returns the number of elements in the vector.

        Returns:
            int: The number of elements.
        """
        ... # Same as __len__
    def capacity(self) -> int:
        """Returns the storage capacity of the vector.

        Returns:
            int: The current capacity.
        """
        ...
    def reserve(self, n: int) -> None:
        """Requests that the vector capacity be at least enough to contain n elements.

        Args:
            n (int): The new capacity.
        """
        ...

class UIntVector(MutableSequence[int]):
    """SWIG wrapper for std::vector<unsigned int>.

    Provides a Pythonic interface to a C++ vector of unsigned integers.
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[int]) -> None: ...
    @overload
    def __init__(self, other: "UIntVector") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for UIntVector.

        Can be initialized empty, with a size, from an iterable, or by copying another UIntVector.
        """
        ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> int: ...
    @overload
    def __getitem__(self, slice_obj: slice) -> "UIntVector": ...
    def __getitem__(self, key: Union[int, slice]) -> Union[int, "UIntVector"]: ...
    @overload
    def __setitem__(self, index: int, value: int) -> None: ...
    @overload
    def __setitem__(self, slice_obj: slice, value: Iterable[int]) -> None: ...
    def __setitem__(self, key: Union[int, slice], value: Any) -> None: ...
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def append(self, x: int) -> None: ...
    def pop(self, index: Optional[int] = None) -> int: ...
    def clear(self) -> None: ...
    def extend(self, iterable: Iterable[int]) -> None: ...
    def insert(self, index: int, value: int) -> None: ...
    def push_back(self, x: int) -> None: ...
    def pop_back(self) -> None: ...
    def empty(self) -> bool: ...
    def size(self) -> int: ...
    def capacity(self) -> int: ...
    def reserve(self, n: int) -> None: ...

class IntVector(MutableSequence[int]):
    """SWIG wrapper for std::vector<int>.

    Provides a Pythonic interface to a C++ vector of integers.
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[int]) -> None: ...
    @overload
    def __init__(self, other: "IntVector") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for IntVector.

        Can be initialized empty, with a size, from an iterable, or by copying another IntVector.
        """
        ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> int: ...
    @overload
    def __getitem__(self, slice_obj: slice) -> "IntVector": ...
    def __getitem__(self, key: Union[int, slice]) -> Union[int, "IntVector"]: ...
    @overload
    def __setitem__(self, index: int, value: int) -> None: ...
    @overload
    def __setitem__(self, slice_obj: slice, value: Iterable[int]) -> None: ...
    def __setitem__(self, key: Union[int, slice], value: Any) -> None: ...
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def append(self, x: int) -> None: ...
    def pop(self, index: Optional[int] = None) -> int: ...
    def clear(self) -> None: ...
    def extend(self, iterable: Iterable[int]) -> None: ...
    def insert(self, index: int, value: int) -> None: ...
    def push_back(self, x: int) -> None: ...
    def pop_back(self) -> None: ...
    def empty(self) -> bool: ...
    def size(self) -> int: ...
    def capacity(self) -> int: ...
    def reserve(self, n: int) -> None: ...

class FloatVector(MutableSequence[float]):
    """SWIG wrapper for std::vector<float>.

    Provides a Pythonic interface to a C++ vector of floats.
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[float]) -> None: ...
    @overload
    def __init__(self, other: "FloatVector") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for FloatVector.

        Can be initialized empty, with a size, from an iterable, or by copying another FloatVector.
        """
        ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> float: ...
    @overload
    def __getitem__(self, slice_obj: slice) -> "FloatVector": ...
    def __getitem__(self, key: Union[int, slice]) -> Union[float, "FloatVector"]: ...
    @overload
    def __setitem__(self, index: int, value: float) -> None: ...
    @overload
    def __setitem__(self, slice_obj: slice, value: Iterable[float]) -> None: ...
    def __setitem__(self, key: Union[int, slice], value: Any) -> None: ...
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def append(self, x: float) -> None: ...
    def pop(self, index: Optional[int] = None) -> float: ...
    def clear(self) -> None: ...
    def extend(self, iterable: Iterable[float]) -> None: ...
    def insert(self, index: int, value: float) -> None: ...
    def push_back(self, x: float) -> None: ...
    def pop_back(self) -> None: ...
    def empty(self) -> bool: ...
    def size(self) -> int: ...
    def capacity(self) -> int: ...
    def reserve(self, n: int) -> None: ...

class DoubleVector(MutableSequence[float]):
    """SWIG wrapper for std::vector<double>.

    Provides a Pythonic interface to a C++ vector of doubles (represented as floats in Python).
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[float]) -> None: ...
    @overload
    def __init__(self, other: "DoubleVector") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for DoubleVector.

        Can be initialized empty, with a size, from an iterable, or by copying another DoubleVector.
        """
        ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> float: ...
    @overload
    def __getitem__(self, slice_obj: slice) -> "DoubleVector": ...
    def __getitem__(self, key: Union[int, slice]) -> Union[float, "DoubleVector"]: ...
    @overload
    def __setitem__(self, index: int, value: float) -> None: ...
    @overload
    def __setitem__(self, slice_obj: slice, value: Iterable[float]) -> None: ...
    def __setitem__(self, key: Union[int, slice], value: Any) -> None: ...
    def __delitem__(self, key: Union[int, slice]) -> None: ...
    def append(self, x: float) -> None: ...
    def pop(self, index: Optional[int] = None) -> float: ...
    def clear(self) -> None: ...
    def extend(self, iterable: Iterable[float]) -> None: ...
    def insert(self, index: int, value: float) -> None: ...
    def push_back(self, x: float) -> None: ...
    def pop_back(self) -> None: ...
    def empty(self) -> bool: ...
    def size(self) -> int: ...
    def capacity(self) -> int: ...
    def reserve(self, n: int) -> None: ...

# SWIG-generated template specializations for std::map
class MapUIntBool(MutableMapping[int, bool]):
    """SWIG wrapper for std::map<unsigned int, bool>.

    Provides a Pythonic dictionary-like interface to a C++ map.
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, mapping: Union[Mapping[int, bool], Iterable[Tuple[int, bool]]]) -> None: ...
    @overload
    def __init__(self, other: "MapUIntBool") -> None: ... # Copy constructor
    def __init__(self, *args: Any) -> None:
        """Constructor for MapUIntBool.

        Can be initialized empty, from a mapping/iterable, or by copying another MapUIntBool.
        """
        ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: int) -> bool: ...
    def __setitem__(self, key: int, value: bool) -> None: ...
    def __delitem__(self, key: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def clear(self) -> None:
        """Removes all elements from the map."""
        ...
    def empty(self) -> bool:
        """Checks if the map is empty.

        Returns:
            bool: True if the map is empty, False otherwise.
        """
        ...
    def size(self) -> int:
        """Returns the number of elements in the map.

        Returns:
            int: The number of elements.
        """
        ...

class MapUIntInt(MutableMapping[int, int]):
    """SWIG wrapper for std::map<unsigned int, int>.

    Provides a Pythonic dictionary-like interface to a C++ map.
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, mapping: Union[Mapping[int, int], Iterable[Tuple[int, int]]]) -> None: ...
    @overload
    def __init__(self, other: "MapUIntInt") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for MapUIntInt.

        Can be initialized empty, from a mapping/iterable, or by copying another MapUIntInt.
        """
        ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: int) -> int: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __delitem__(self, key: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def clear(self) -> None: ...
    def empty(self) -> bool: ...
    def size(self) -> int: ...

# SWIG-generated template specializations for std::array
# ETHERNETSCANNER_SCANXMAX is a C++ constant, size is fixed
class IntArray(MutableSequence[int]): # Fixed-size, but elements are mutable
    """SWIG wrapper for a C++ fixed-size array of integers (e.g., std::array<int, N>).

    The size is determined by the C++ definition (e.g., ETHERNETSCANNER_SCANXMAX).
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[int]) -> None: ... # If SWIG supports init from Python sequence
    @overload
    def __init__(self, other: "IntArray") -> None: ... # Copy constructor
    def __init__(self, *args: Any) -> None:
        """Constructor for IntArray.

        Typically initialized by SWIG. May support initialization from an iterable if configured.
        """
        ...

    def __len__(self) -> int:
        """Returns the fixed size of the array.

        Returns:
            int: The size of the array.
        """
        ... # Returns ETHERNETSCANNER_SCANXMAX
    @overload
    def __getitem__(self, index: int) -> int: ...
    @overload
    def __getitem__(self, slice_obj: slice) -> List[int]: ... # Slicing std::array typically returns a new sequence (list)
    def __getitem__(self, key: Union[int, slice]) -> Union[int, List[int]]: ...
    @overload
    def __setitem__(self, index: int, value: int) -> None: ...
    @overload
    def __setitem__(self, slice_obj: slice, value: Iterable[int]) -> None: ...
    def __setitem__(self, key: Union[int, slice], value: Any) -> None: ...
    # __delitem__ is not applicable to std::array
    def fill(self, value: int) -> None:
        """Fills the entire array with a specified value.

        Args:
            value (int): The value to fill the array with.
        """
        ...
    def empty(self) -> bool:
        """Checks if the array is empty (size is 0).

        Returns:
            bool: True if the array size is 0, False otherwise.
        """
        ... # Only if ETHERNETSCANNER_SCANXMAX can be 0
    def size(self) -> int:
        """Returns the fixed size of the array.

        Returns:
            int: The size of the array.
        """
        ...
    def front(self) -> int:
        """Accesses the first element.

        Returns:
            int: The first element of the array.
        """
        ...
    def back(self) -> int:
        """Accesses the last element.

        Returns:
            int: The last element of the array.
        """
        ...

class DoubleArray(MutableSequence[float]): # Fixed-size
    """SWIG wrapper for a C++ fixed-size array of doubles (e.g., std::array<double, N>).

    The size is determined by the C++ definition. Elements are floats in Python.
    """
    thisown: property
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[float]) -> None: ...
    @overload
    def __init__(self, other: "DoubleArray") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for DoubleArray."""
        ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> float: ...
    @overload
    def __getitem__(self, slice_obj: slice) -> List[float]: ...
    def __getitem__(self, key: Union[int, slice]) -> Union[float, List[float]]: ...
    @overload
    def __setitem__(self, index: int, value: float) -> None: ...
    @overload
    def __setitem__(self, slice_obj: slice, value: Iterable[float]) -> None: ...
    def __setitem__(self, key: Union[int, slice], value: Any) -> None: ...
    def fill(self, value: float) -> None:
        """Fills the entire array with a specified value.

        Args:
            value (float): The value to fill the array with.
        """
        ...
    def empty(self) -> bool: ...
    def size(self) -> int: ...
    def front(self) -> float: ...
    def back(self) -> float: ...

# Application-specific classes
class waam_error(RuntimeError): # Assuming it derives from std::runtime_error
    """Custom exception class for WAAM API errors.

    Likely wraps a C++ std::runtime_error or similar.
    """
    thisown: property
    @overload
    def __init__(self, what_arg: str) -> None: ...
    @overload
    def __init__(self, what_arg: str, location: Any) -> None: ... # std::source_location is tricky
    def __init__(self, *args: Any) -> None:
        """Constructor for waam_error.

        Args:
            what_arg (str): Error message string.
            location (Any, optional): Source location information.
        """
        ...
    def what(self) -> str:
        """Returns the error message.

        Returns:
            str: The error message string.
        """
        ...

class Settings:
    """Holds configuration settings for the WAAM API.

    Provides access to various parameters like IP addresses, ports, and operational limits.
    Configuration is typically loaded from a 'config.yaml' file.

    Default Robot IPs:
        Arc Robot: 192.168.254.7
        Collaborative Robot: 192.168.255.101
    Default Robot Ports:
        11000, 12000, 13000, 15000 (specific usage depends on port).
    Default Laser IPs:
        Arc Robot Laser: 192.168.255.8
        Collaborative Robot Laser: 192.168.100.1
    Default Laser Port: 32001.

    Examples:
    ```python
    s = Settings()
    robot_ip = s.get_robot_ip()
    laser_port = s.get_laser_port()
    print(f"Robot IP: {robot_ip}, Laser Port: {laser_port}")
    ```
    """
    thisown: property
    def __init__(self) -> None:
        """Default constructor for Settings.

        Loads settings, typically from a 'config.yaml' file.
        If 'config.yaml' is not found or incomplete, may use hardcoded defaults.
        """
        ...
    def get_robot_ip(self) -> str:
        """Gets the robot IP address from settings.

        Returns:
            str: Robot IP address string (e.g., "192.168.254.7").
        """
        ...
    def get_laser_ip(self) -> str:
        """Gets the laser scanner IP address from settings.

        Returns:
            str: Laser IP address string (e.g., "192.168.255.8").
        """
        ...
    def get_laser_port(self) -> str: # Port can be a service name or number, hence string
        """Gets the laser scanner port from settings.

        Returns:
            str: Laser port string (e.g., "32001").
        """
        ...
    def get_coord_port(self) -> int:
        """Gets the port number for coordinate data from settings.

        Returns:
            int: Coordinate data port number (e.g., one of 11000, 12000, 13000, 15000).
        """
        ...
    def get_io_port(self) -> int:
        """Gets the port number for I/O operations from settings.

        Returns:
            int: I/O port number (e.g., one of 11000, 12000, 13000, 15000).
        """
        ...
    def get_var_port(self) -> int:
        """Gets the port number for variable access from settings.

        Returns:
            int: Variable access port number (e.g., one of 11000, 12000, 13000, 15000).
        """
        ...
    def get_laser_is_active(self) -> bool:
        """Checks if the laser is configured to be active in settings.

        Returns:
            bool: True if laser is active, False otherwise.
        """
        ...
    def get_robot_is_active(self) -> bool:
        """Checks if the robot is configured to be active in settings.

        Returns:
            bool: True if robot is active, False otherwise.
        """
        ...
    def get_laser_min_x(self) -> float:
        """Gets the minimum X-axis value for laser data filtering from settings.

        Returns:
            float: Minimum X value.
        """
        ...
    def get_laser_max_x(self) -> float:
        """Gets the maximum X-axis value for laser data filtering from settings.

        Returns:
            float: Maximum X value.
        """
        ...
    def get_laser_min_z(self) -> float:
        """Gets the minimum Z-axis value for laser data filtering from settings.

        Returns:
            float: Minimum Z value.
        """
        ...
    def get_laser_max_z(self) -> float:
        """Gets the maximum Z-axis value for laser data filtering from settings.

        Returns:
            float: Maximum Z value.
        """
        ...
    def get_laser_min_intensity(self) -> int:
        """Gets the minimum intensity value for laser data filtering from settings.

        Returns:
            int: Minimum intensity value.
        """
        ...
    def get_laser_max_intensity(self) -> int:
        """Gets the maximum intensity value for laser data filtering from settings.

        Returns:
            int: Maximum intensity value.
        """
        ...
    def get_take_each(self) -> int:
        """Gets the 'take each Nth point' value for laser data subsampling from settings.

        Returns:
            int: Subsampling factor (e.g., 1 for all points, 2 for every other point).
        """
        ...

class Cache:
    """Represents a cache entry.

    Used for storing named data strings.
    """
    thisown: property
    def __init__(self, name: str, data: str) -> None:
        """Constructor for Cache.

        Args:
            name (str): The name of the cache entry.
            data (str): The data string to cache.
        """
        ...

class Info:
    """Base class for data structures holding common information like ID and timestamps."""
    thisown: property
    id: int
    """Unique identifier for the data packet or event."""
    delta_tm: int
    """Time delta, possibly in microseconds or milliseconds, meaning depends on context."""
    received_tm: int # uint64_t, often a large integer timestamp (e.g., microseconds since epoch)
    """Timestamp of when the data was received, typically a high-resolution timestamp."""

    def __init__(self) -> None:
        """Default constructor for Info."""
        ...
    def GetTimeStr(self) -> str:
        """Gets the received time as a formatted string (C++ std::chrono based).

        The exact format depends on the C++ implementation.

        Returns:
            str: Formatted timestamp string.
        """
        ...
    def GetPythonTimeStr(self) -> str:
        """Gets the received time as a Python-friendly formatted string (likely ISO format UTC).

        Returns:
            str: Python-friendly formatted timestamp string (e.g., ISO 8601).
        """
        ...
    def SetTime(self, time_str: str) -> None:
        """Sets the received time from a C++ style formatted string.

        Args:
            time_str (str): Timestamp string (format expected by C++ backend).
        """
        ...
    def SetPythonTime(self, time_str_utc: str) -> None:
        """Sets the received time from a Python-friendly (UTC ISO format) string.

        Args:
            time_str_utc (str): Timestamp string in UTC (preferably ISO 8601 format).
        """
        ...

class ScanBasis:
    """Base class for scanning operations.

    Manages the state of a continuous or triggered data acquisition process.
    """
    thisown: property
    store_in_csv: bool
    """Flag indicating whether scanned data should be stored in a CSV file."""

    def __init__(self) -> None:
        """Default constructor for ScanBasis."""
        ...
    def __swig_destroy__(self) -> None:
        """SWIG-managed destructor."""
        ...
    def Stop(self) -> None:
        """Stops the scanning process.

        Sets a flag to terminate any ongoing scanning threads or operations.
        """
        ...
    def Start(self) -> None:
        """Starts the scanning process.

        Initiates data acquisition, possibly in a new thread.
        """
        ...
    def Destroy(self) -> None:
        """Cleans up resources associated with the scan.

        Should be called to ensure proper termination and resource release.
        """
        ...
    def IsNew(self) -> bool:
        """Checks if new data is available from the scan.

        Returns:
            bool: True if new data has been acquired since the last check, False otherwise.
        """
        ...
    def Store(self, store_in_csv: bool) -> None:
        """Sets whether to store scanned data in a CSV file.

        Args:
            store_in_csv (bool): True to enable CSV storage, False to disable.
        """
        ...
    def SetIsNew(self, is_new: bool) -> None:
        """Manually sets the 'is_new' flag.

        Args:
            is_new (bool): The new state of the flag.
        """
        ...
    def SetIsActive(self, is_active: bool) -> None:
        """Manually sets the 'is_active' flag for the scan.

        Args:
            is_active (bool): The new state of the activity flag.
        """
        ...
    def SetStopFlag(self, stop_flag: bool) -> None:
        """Manually sets the stop flag for the scan.

        Args:
            stop_flag (bool): True to request scan termination.
        """
        ...
    def GetIsNew(self) -> bool:
        """Gets the current state of the 'is_new' data flag.

        Returns:
            bool: True if new data is available.
        """
        ...
    def GetIsActive(self) -> bool:
        """Gets the current state of the 'is_active' flag.

        Returns:
            bool: True if the scan is currently active.
        """
        ...
    def GetStopFlag(self) -> bool:
        """Gets the current state of the stop flag.

        Returns:
            bool: True if a stop has been requested.
        """
        ...

class MessageQueueCSV:
    """A thread-safe queue for messages intended for CSV logging."""
    thisown: property
    def __init__(self) -> None:
        """Default constructor for MessageQueueCSV."""
        ...
    def push(self, value: str) -> None:
        """Pushes a string message onto the queue.

        Args:
            value (str): The string message to add.
        """
        ...
    def pop(self) -> str:
        """Pops a string message from the queue.

        Blocks if the queue is empty until a message is available.

        Returns:
            str: The string message from the front of the queue.
        """
        ...
    def size(self) -> int:
        """Returns the current number of messages in the queue.

        Returns:
            int: The size of the queue.
        """
        ...

class CSV:
    """Utility class for handling CSV file operations.

    Manages creation, writing, and saving of CSV data.
    """
    thisown: property
    def __init__(self, csv_name: str, header: str) -> None:
        """Constructor for CSV.

        Args:
            csv_name (str): The base name for the CSV file (without extension).
            header (str): The header string for the CSV file (comma-separated values).
        """
        ...
    def __swig_destroy__(self) -> None:
        """SWIG-managed destructor."""
        ...
    def CreateNewFile(self) -> None:
        """Creates a new CSV file, potentially with a timestamped name, and writes the header."""
        ...
    def CleanUpEmptyFiles(self) -> None:
        """Removes all empty CSV files in the folder."""
        ...
    def Save(self, csv_data_row: str, in_new_file: bool = False) -> None:
        """Saves a row of CSV data.

        Can optionally create a new file before saving.

        Args:
            csv_data_row (str): A single string representing a row of comma-separated values.
            in_new_file (bool): If True, creates a new file before saving this row. Defaults to False.
        """
        ...
    def SaveThread(self) -> None:
        """Starts a separate thread for saving CSV data from a queue (likely MessageQueueCSV)."""
        ...
    def ToCSV(self, data: List[str]) -> str:
        """Converts a list of strings into a single CSV formatted string.

        Args:
            data (List[str]): A list of strings to be joined by commas.

        Returns:
            str: A comma-separated string.
        """
        ...
    @staticmethod
    @overload
    def GetSetFolder() -> str: ...
    @staticmethod
    @overload
    def GetSetFolder(folder_name: str) -> str: ...
    @staticmethod
    def GetSetFolder(folder_name: str = "") -> str:
        """Gets or sets the default folder for saving CSV files.

        If folder_name is provided, it sets the folder and returns it.
        If folder_name is empty, it returns the current folder.

        Args:
            folder_name (str, optional): The name of the folder to set.

        Returns:
            str: The current or newly set CSV folder path.
        """
        ... # Implementation

class Response(Info):
    """Represents a response from a device or operation, typically a request-reply pair.

    Inherits ID and timestamp information from Info.
    """
    thisown: property
    request_: str
    """The original request string sent to the device."""
    response_: str
    """The response string received from the device."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, resp: str) -> None: ...
    @overload
    def __init__(self, req: str, resp: str) -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for Response.

        Can be initialized empty, with just a response, or with a request and response.

        Args:
            resp (str, optional): The response string.
            req (str, optional): The request string.
        """
        ...
    def split(self, delimiter: str = ',') -> List[str]:
        """Splits the response_ string by a delimiter.

        Args:
            delimiter (str): The delimiter to use for splitting. Defaults to ','.

        Returns:
            List[str]: A list of strings.
        """
        ...

class CoordinateCSV(CSV):
    """Specialized CSV handler for Coordinate data."""
    def __init__(self) -> None:
        """Constructor for CoordinateCSV.

        Initializes with a predefined CSV name and header for coordinate data.
        """
        ...

class Coordinate(Info):
    """Represents a 3D coordinate with orientation (X, Y, Z, Rx, Ry, Rz).

    Inherits ID and timestamp information from Info.
    Coordinates can be in different frames (e.g., Base/World frame, Tool frame, UserN frame).
    The specific frame depends on the context of how the Coordinate object was obtained.
    """
    thisown: property
    x: float; y: float; z: float
    rx: float; ry: float; rz: float
    is_valid: bool
    """Flag indicating if the coordinate data is valid."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, resp: "Response") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for Coordinate.

        Can be initialized empty or parsed from a Response object.

        Args:
            resp ("Response", optional): A Response object containing coordinate data to parse.
        """
        ...
    def Save(self, in_new_file: bool = False) -> None:
        """Saves the coordinate data to a CSV file.

        Uses the CoordinateCSV handler.

        Args:
            in_new_file (bool): If True, creates a new CSV file before saving. Defaults to False.
        """
        ...

class CoordinateScan(ScanBasis):
    """Manages scanning of Coordinate data.

    Inherits from ScanBasis for controlling the scanning process.
    Likely uses a std::shared_ptr for lifetime management in C++.
    """
    thisown: property
    def __init__(self) -> None:
        """Default constructor for CoordinateScan."""
        ...
    def Get(self) -> "Coordinate":
        """Retrieves the latest scanned Coordinate data.

        Marks the current data as not new.

        Returns:
            "Coordinate": The latest Coordinate data.
        """
        ...
    def Set(self, xyz: "Coordinate") -> None:
        """Manually sets the current coordinate data for the scan.

        Used internally or for simulation. Marks data as new.

        Args:
            xyz ("Coordinate"): The Coordinate data to set.
        """
        ...

class LaserCSV(CSV):
    """Specialized CSV handler for LaserCoordinate data."""
    def __init__(self) -> None:
        """Constructor for LaserCSV.

        Initializes with a predefined CSV name and header for laser data.
        """
        ...

class LaserDataFiltered:
    """Represents filtered laser scan data.

    Contains vectors for X, Z coordinates, intensity, and signal width after filtering.
    """
    thisown: property
    id: int
    """ID of the laser scan profile."""
    time: int # Typically a timestamp from the laser scanner's clock
    """Timestamp from the laser scanner for this profile (e.g., microseconds)."""
    time_received: float # Representing std::chrono::system_clock::time_point as a float timestamp
    """Host timestamp when this data was processed/received (e.g., seconds since epoch)."""
    x: DoubleVector
    """Vector of X coordinates of laser points."""
    z: DoubleVector
    """Vector of Z coordinates of laser points."""
    intensity: IntVector
    """Vector of intensity values for each laser point."""
    signal_width: IntVector
    """Vector of signal width values for each laser point (if available)."""

    def __init__(self) -> None:
        """Default constructor for LaserDataFiltered."""
        ...

class FilterStruct:
    """Structure holding parameters for filtering laser data.

    Likely used with std::unique_ptr in C++ for managing its lifetime.
    """
    thisown: property
    min_x: float; max_x: float; min_z: float; max_z: float
    """Min/max X and Z coordinate bounds for filtering."""
    min_intensity: int; max_intensity: int; take_each: int
    """Min/max intensity bounds and subsampling factor ('take_each' Nth point)."""

    def __init__(self) -> None:
        """Default constructor for FilterStruct.

        Initializes filter parameters, possibly to default "accept all" values.
        """
        ...

class LaserData:
    """Represents raw laser scan data from a single profile.

    Uses fixed-size arrays (DoubleArray, IntArray) for raw data.
    """
    thisown: property
    id: int
    """ID of the laser scan profile."""
    time: int # Timestamp from laser
    """Timestamp from the laser scanner for this profile (e.g., microseconds)."""
    time_received: float # Host timestamp
    """Host timestamp when this data was received/processed (e.g., seconds since epoch)."""
    x: DoubleArray
    """Fixed-size array of raw X coordinates."""
    z: DoubleArray
    """Fixed-size array of raw Z coordinates."""
    intensity: IntArray
    """Fixed-size array of raw intensity values."""
    signal_width: IntArray
    """Fixed-size array of raw signal width values."""
    n: int
    """Number of valid points in the current scan profile."""
    prev_n: int
    """Number of valid points in the previous scan profile (used for extrapolation)."""

    def __init__(self) -> None:
        """Default constructor for LaserData."""
        ...
    def Filter(self) -> "LaserDataFiltered":
        """Applies filters (defined by SetFilter) to the raw laser data.

        Returns:
            "LaserDataFiltered": A LaserDataFiltered object containing the filtered points.
        """
        ...
    def Extrapolate(self) -> None:
        """Performs extrapolation on the laser data if the number of points (n) is less than expected.

        Fills missing data based on previous points or other logic.
        """
        ...
    @staticmethod
    def SetFilter(filter_params: "FilterStruct") -> None:
        """Sets the global filter parameters to be used by the Filter() method.

        Args:
            filter_params ("FilterStruct"): A FilterStruct object containing the filter settings.
        """
        ...

class LaserCoordinate(Info):
    """Represents processed laser coordinate data (a collection of points from a scan).

    Inherits ID and timestamp information from Info. Uses dynamic vectors.
    """
    thisown: property
    x: DoubleVector
    """Vector of X coordinates of laser points."""
    z: DoubleVector
    """Vector of Z coordinates of laser points."""
    intensity: IntVector
    """Vector of intensity values for each laser point."""
    is_valid: bool
    """Flag indicating if the laser coordinate data is valid."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, data: "LaserData") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for LaserCoordinate.

        Can be initialized empty or from a raw LaserData object (implies filtering).

        Args:
            data ("LaserData", optional): A LaserData object to process into LaserCoordinate.
        """
        ...
    def Save(self, in_new_file: bool = False) -> None:
        """Saves the laser coordinate data to a CSV file.

        Uses the LaserCSV handler.

        Args:
            in_new_file (bool): If True, creates a new CSV file before saving. Defaults to False.
        """
        ...

class LaserCoordinateScan(ScanBasis):
    """Manages scanning of LaserCoordinate data.

    Inherits from ScanBasis.
    """
    thisown: property
    clean_buf_counter: int
    """Counter used for periodic buffer cleaning or other maintenance tasks."""
    MAX_CLEAN_BUF_COUNTER: int # const
    """Maximum value for clean_buf_counter before an action is triggered."""

    def __init__(self) -> None:
        """Default constructor for LaserCoordinateScan."""
        ...
    def Get(self) -> "LaserCoordinate":
        """Retrieves the latest scanned LaserCoordinate data.

        Returns:
            "LaserCoordinate": The latest LaserCoordinate data.
        """
        ...
    def Set(self, xyz: "LaserCoordinate") -> None:
        """Manually sets the current laser coordinate data for the scan.

        Args:
            xyz ("LaserCoordinate"): The LaserCoordinate data to set.
        """
        ...

class RobotLaserCoordinateCSV(CSV):
    """Specialized CSV handler for RobotLaserCoordinate data."""
    def __init__(self) -> None:
        """Constructor for RobotLaserCoordinateCSV.

        Initializes with a predefined CSV name and header for combined robot and laser data.
        """
        ...

class RobotLaserCoordinate(Info):
    """Represents combined robot coordinates and laser scan data at a specific moment.

    Inherits ID and timestamp information from Info.
    The robot coordinates are typically in a specific frame (e.g., Base 0, Base 3),
    and laser data is transformed accordingly.
    """
    thisown: property
    x: float; y: float; z: float
    """Robot's X, Y, Z coordinates."""
    rx: float; ry: float; rz: float
    """Robot's Rx, Ry, Rz orientation."""
    x_arr: DoubleVector
    """Vector of X coordinates from the laser scan, transformed to robot's coordinate system."""
    z_arr: DoubleVector
    """Vector of Z coordinates from the laser scan, transformed to robot's coordinate system."""
    i_arr: IntVector
    """Vector of intensity values from the laser scan."""
    is_valid: bool
    """Flag indicating if the combined data is valid."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, resp: "Response", data: "LaserData") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for RobotLaserCoordinate.

        Can be initialized empty or from a robot Response and raw LaserData.

        Args:
            resp ("Response", optional): Robot's coordinate data as a Response object.
            data ("LaserData", optional): Raw laser data.
        """
        ...
    def Save(self, in_new_file: bool = False) -> None:
        """Saves the combined robot and laser coordinate data to a CSV file.

        Uses RobotLaserCoordinateCSV handler.

        Args:
            in_new_file (bool): If True, creates a new CSV file before saving. Defaults to False.
        """
        ...
    @staticmethod
    def GetLaserCSV() -> "LaserCSV":
        """Gets the LaserCSV instance used for saving individual laser data.

        Returns:
            "LaserCSV": The LaserCSV instance.
        """
        ...
    @staticmethod
    def GetCoordCSV() -> "CoordinateCSV":
        """Gets the CoordinateCSV instance used for saving individual robot coordinate data.

        Returns:
            "CoordinateCSV": The CoordinateCSV instance.
        """
        ...

class RobotLaserCoordinateScan(ScanBasis):
    """Manages scanning of combined RobotLaserCoordinate data.

    Inherits from ScanBasis.
    """
    thisown: property
    clean_buf_counter: int
    MAX_CLEAN_BUF_COUNTER: int # const

    def __init__(self) -> None:
        """Default constructor for RobotLaserCoordinateScan."""
        ...
    def Get(self) -> "RobotLaserCoordinate":
        """Retrieves the latest scanned RobotLaserCoordinate data.

        Returns:
            "RobotLaserCoordinate": The latest RobotLaserCoordinate data.
        """
        ...
    def Set(self, xyz: "RobotLaserCoordinate") -> None:
        """Manually sets the current combined data for the scan.

        Args:
            xyz ("RobotLaserCoordinate"): The RobotLaserCoordinate data to set.
        """
        ...

class Dout(Info):
    """Represents the state of a digital output (DOUT) pin.

    Inherits ID and timestamp information from Info.
    """
    thisown: property
    index: int
    """The index or ID of the digital output pin."""
    state: bool
    """The state of the pin (True for ON, False for OFF)."""
    is_valid: bool
    """Flag indicating if the Dout data is valid."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, indx: int, resp: "Response") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for Dout.

        Can be initialized empty or parsed from an index and a Response object.

        Args:
            indx (int, optional): The index of the DOUT pin.
            resp ("Response", optional): A Response object containing the DOUT state to parse.
        """
        ...
    def Save(self, in_new_file: bool = False) -> None:
        """Saves the Dout state to a CSV file.

        Args:
            in_new_file (bool): If True, creates a new CSV file before saving. Defaults to False.

        Note:
            This implies a DoutCSV class might exist or a generic CSV handler is used.
        """
        ...

class Var(Info):
    """Represents a generic variable read from or written to a device.

    Inherits ID and timestamp information from Info.
    """
    thisown: property
    index: int
    """The index or ID of the variable."""
    type: int # Could be an enum in C++: eBYTE, eINTEGER, eDOUBLE etc.
    """The data type of the variable (e.g., byte, integer, double).
    Often represented by an integer code corresponding to an enum.
    """
    value: str
    """The value of the variable, stored as a string."""
    is_valid: bool
    """Flag indicating if the Var data is valid."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, indx: int, t: int, resp: "Response") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for Var.

        Can be initialized empty or parsed from an index, type, and a Response object.

        Args:
            indx (int, optional): The index of the variable.
            t (int, optional): The type code of the variable.
            resp ("Response", optional): A Response object containing the variable value to parse.
        """
        ...
    def ToByte(self) -> int: # Assuming byte is represented as int in Python
        """Converts the string value to a byte (integer 0-255).

        Returns:
            int: The byte value as an integer.

        Raises:
            ValueError: If the string value cannot be converted to a byte.
        """
        ...
    def ToInteger(self) -> int:
        """Converts the string value to an integer.

        Returns:
            int: The integer value.

        Raises:
            ValueError: If the string value cannot be converted to an integer.
        """
        ...
    def ToDouble(self) -> float:
        """Converts the string value to a double (float).

        Returns:
            float: The float value.

        Raises:
            ValueError: If the string value cannot be converted to a float.
        """
        ...

class WeldParametrs(Info): # Assuming inheritance from Info
    """Represents welding parameters.

    Contains information about the welding process such as current, voltage, and wire feed speed.
    """
    thisown: property
    current: float
    """Welding current, typically in Amperes (A)."""
    voltage: float
    """Welding voltage, typically in Volts (V)."""
    wfs: float
    """Wire Feed Speed, typically in meters per minute (m/min) or inches per minute (ipm)."""
    is_welded: bool
    """Flag indicating if welding is currently active or was active for this parameter set."""
    is_valid: bool
    """Flag indicating if the WeldParametrs data is valid and can be reliably used."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, resp: "Response") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for WeldParametrs.

        Can be initialized empty or parsed from a Response object.

        Args:
            resp ("Response", optional): A Response object containing WeldParametrs data to parse.
        """
        ...

class JobParametrs(Info): # Assuming inheritance from Info
    """Represents parameters and state of a robot job or program.

    Contains details like job name, current execution line, step, operational state,
    and active coordinate frames (e.g., Base/World frame, Tool frame, UserN frame via 'frame' attribute) and tools.
    The specific active frame or tool depends on the context of how the JobParametrs object was obtained.
    """
    thisown: property
    """SWIG-generated attribute for memory management."""
    name: str
    """Name of the currently executing or selected job/program."""
    line: int
    """Current line number being executed in the job/program."""
    step: int
    """Current step number or sub-instruction within the current line of the job/program."""
    in_hold: bool
    """Flag indicating if the job execution is currently in a hold state (paused)."""
    in_work: bool
    """Flag indicating if the robot/system is actively performing work as part of the job."""
    frame: int
    """Identifier for the currently active coordinate frame (e.g., user frame number)."""
    tool: int
    """Identifier for the currently active tool (e.g., tool center point - TCP number)."""
    is_valid: bool
    """Flag indicating if the JobParametrs data is valid and can be reliably used."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, resp: "Response") -> None: ...
    def __init__(self, *args: Any) -> None:
        """Constructor for JobParametrs.

        Can be initialized empty or parsed from a Response object.

        Args:
            resp ("Response", optional): A Response object containing JobParametrs data to parse.
        """
        ...
        
class RobotData:
    """Represents a raw data packet received from the robot."""
    thisown: property
    id: int
    """Sequence ID or identifier for the data packet."""
    time_us: int # Timestamp in microseconds, likely from robot controller
    """Timestamp in microseconds, typically from the robot's internal clock."""
    time_received: float # Host timestamp
    """Host timestamp when this data was received (e.g., seconds since epoch)."""
    data: str
    """The raw data string received from the robot."""

    def __init__(self) -> None:
        """Default constructor for RobotData."""
        ...

class RobotMessage: # This seems similar to RobotData, maybe a higher-level abstraction or for specific message types
    """Represents a message from the robot, possibly more structured than RobotData."""
    thisown: property
    id: int
    time: float # std::chrono::steady_clock::time_point
    """Timestamp using a steady clock, for measuring intervals (e.g., seconds)."""
    time_received: float
    """Host timestamp when this message was received (e.g., seconds since epoch)."""
    data: str
    """The message content as a string."""

    def __init__(self) -> None:
        """Default constructor for RobotMessage."""
        ...

class RobotClientsInit: # Placeholder for potential global initialization of robot clients
    """Helper class for initializing robot client components.

    May handle setup for multiple robot communication channels.
    """
    thisown: property
    def __init__(self) -> None:
        """Default constructor for RobotClientsInit."""
        ...

class RobotClient:
    """Client for communicating with a robot controller.

    Provides methods to send commands and receive data.
    Default Robot IPs: Arc Robot (192.168.254.7), Collaborative Robot (192.168.255.101).
    Robot Ports: 11000, 12000, 13000, 15000 (specific port usage defined by robot controller and API implementation).
    """
    thisown: property
    def __init__(self, ip: str, port: int) -> None:
        """Constructor for RobotClient.

        Establishes a connection to the robot at the given IP and port.

        Args:
            ip (str): The IP address of the robot controller (e.g., "192.168.254.7").
            port (int): The port number for communication (e.g., 11000).

        Examples:
        ```python
        settings = Settings()
        robot_ip = settings.get_robot_ip()
        coord_port = settings.get_coord_port()
        r_client = RobotClient(robot_ip, coord_port)
        print(f"RobotClient created for {r_client.GetIP()}:{r_client.GetPort()}")
        ```
        """
        ...
    def __swig_destroy__(self) -> None:
        """SWIG-managed destructor.

        Ensures connection is closed and resources are released.
        """
        ...
    def SendReceive(self, data: str, buff_size: int = 1024) -> "RobotData":
        """Sends data to the robot and receives a response.

        This is typically a synchronous operation.

        Args:
            data (str): The command or data string to send to the robot.
            buff_size (int): The size of the buffer for receiving the response. Defaults to 1024.

        Returns:
            "RobotData": A RobotData object containing the response from the robot.

        Examples:
        ```python
        command_to_send = "1,1,1,1" # Example command
        response = r_client.SendReceive(command_to_send)
        print(f"Response: {response.data}")
        ```
        """
        ...
    def Reconnect(self, ip: str, port_str: str) -> None: # port_str suggests it might be a service name too
        """Attempts to reconnect to the robot.

        Closes any existing connection and establishes a new one.

        Args:
            ip (str): The IP address of the robot controller.
            port_str (str): The port number or service name for communication (e.g., "11000").

        Note:
            The original `RobotClient` constructor took `port: int`. This method takes `port_str: str`.
            This might indicate flexibility in how the port is specified for reconnection.

        Examples:
        ```python
        # Assuming r_client is an initialized RobotClient
        # if not r_client.is_connected(): # Fictional method
        r_client.Reconnect(r_client.GetIP(), str(r_client.GetPort()))
        print("Reconnected.")
        ```
        """
        ...
    def GetIP(self) -> str:
        """Gets the IP address the client is currently configured for.

        Returns:
            str: The IP address string.
        """
        ...
    def GetPort(self) -> int: # Assuming it returns the numeric port if connected or configured
        """Gets the port number the client is currently configured for.

        Returns:
            int: The port number.
        """
        ...

class LaserMessage: # Similar to RobotMessage, but for laser
    """Represents a message related to the laser scanner."""
    thisown: property
    id: int
    time: float # std::chrono::steady_clock::time_point
    """Timestamp using a steady clock (e.g., seconds)."""
    def __init__(self) -> None:
        """Default constructor for LaserMessage."""
        ...

class LaserClient:
    """Client for communicating with a laser scanner.

    Provides methods to send commands, configure the scanner, and receive scan data.
    Default Laser IPs: Arc Robot Laser (192.168.255.8), Collaborative Robot Laser (192.168.100.1).
    Default Laser Port: 32001.
    """
    thisown: property
    def __init__(self, ip: str, port: str) -> None:
        """Constructor for LaserClient.

        Establishes a connection to the laser scanner.

        Args:
            ip (str): The IP address of the laser scanner (e.g., "192.168.255.8").
            port (str): The port number or service name for communication (e.g., "32001").

        Examples:
        ```python
        settings = Settings()
        laser_ip = settings.get_laser_ip()
        laser_port_str = settings.get_laser_port()
        l_client = LaserClient(laser_ip, laser_port_str)
        print(f"LaserClient created for {l_client.GetIP()}:{l_client.GetPort()}")
        ```
        """
        ...
    def __swig_destroy__(self) -> None:
        """SWIG-managed destructor.

        Ensures connection is closed and resources are released.
        """
        ...
    def SetLimits(self, min_x: float, max_x: float, min_z: float, max_z: float, min_intensity: int, max_intensity: int) -> None:
        """Sets the filtering limits for laser data processing.

        These limits are likely used by the `LaserData.Filter()` method or an internal filter.

        Args:
            min_x (float): Minimum X coordinate.
            max_x (float): Maximum X coordinate.
            min_z (float): Minimum Z coordinate.
            max_z (float): Maximum Z coordinate.
            min_intensity (int): Minimum intensity value.
            max_intensity (int): Maximum intensity value.

        Examples:
        ```python
        l_client.SetLimits(-100.0, 100.0, 50.0, 200.0, 10, 250)
        ```
        """
        ...
    @overload
    def Send(self) -> None: ... # From C++ header, parameterless overload for some commands
    @overload
    def Send(self, command: str) -> None: ...
    def Send(self, *args: Any) -> None:
        """NOT USED! Sends a command to the laser scanner.

        Can be parameterless for certain predefined commands or take a command string.

        Args:
            command (str, optional): The command string to send.
        """
        ... # Actual implementation
    def Receive(self) -> "LaserData":
        """Receives a raw laser data profile from the scanner.

        This is typically a blocking call waiting for the next scan profile.

        Returns:
            "LaserData": A LaserData object containing the raw scan profile.

        Examples:
        ```python
        # Assuming l_client is an initialized LaserClient and scanner is transmitting
        raw_profile = l_client.Receive()
        print(f"Received profile ID: {raw_profile.id}")
        # Filter data if needed
        filter_settings = FilterStruct()
        filter_settings.take_each = 1
        LaserData.SetFilter(filter_settings) # Static method call
        filtered_data = raw_profile.Filter()
        ```
        """
        ...
    def Reconnect(self, ip: str, port: str) -> None:
        """Attempts to reconnect to the laser scanner.

        Closes any existing connection and establishes a new one.

        Args:
            ip (str): The IP address of the laser scanner.
            port (str): The port number or service name for communication.

        Examples:
        ```python
        l_client.Reconnect(l_client.GetIP(), l_client.GetPort())
        print("Laser reconnected.")
        ```
        """
        ...

    # Laser Command Functions (as per provided pyi and common laser scanner APIs)
    # These are specific command wrappers, often calling Send() internally.
    def SetReboot(self) -> None:
        """NOT USED! Sends a command to reboot the laser scanner.

        Warning:
            Use with caution, as this will interrupt operation.
        """
        ...
    def SetExposureTime(self, exposure_time_us: int) -> None:
        """NOT USED! Sets the exposure time for the scanner's sensor.

        Args:
            exposure_time_us (int): Exposure time in microseconds.
        """
        ...
    def SetAutoExposureMode(self, enabled: bool) -> None:
        """Enables or disables auto exposure mode.

        Args:
            enabled (bool): True to enable auto exposure, False for manual.

        Examples:
        ```python
        l_client.SetAutoExposureMode(True)
        ```
        """
        ...
    def SetAutoExposureTimeMin(self, min_time_us: int) -> None:
        """NOT USED! Sets the minimum exposure time for auto exposure mode.

        Args:
            min_time_us (int): Minimum exposure time in microseconds.
        """
        ...
    def SetAutoExposureTimeMax(self, max_time_us: int) -> None:
        """NOT USED! Sets the maximum exposure time for auto exposure mode.

        Args:
            max_time_us (int): Maximum exposure time in microseconds.
        """
        ...
    def SetAutoExposureIntensityRangeMin(self, min_intensity: int) -> None:
        """NOT USED! Sets the minimum target intensity for auto exposure.

        Args:
            min_intensity (int): Minimum target intensity value.
        """
        ...
    def SetAutoExposureIntensityRangeMax(self, max_intensity: int) -> None:
        """NOT USED! Sets the maximum target intensity for auto exposure.

        Args:
            max_intensity (int): Maximum target intensity value.
        """
        ...
    def SetAutoExposureRangeXMin(self, min_x: int) -> None:
        """NOT USED! Sets the minimum X coordinate (in sensor pixels/units) for the auto exposure ROI.

        Args:
            min_x (int): Minimum X for auto exposure region of interest.
        """
        ...
    def SetAutoExposureRangeXMax(self, max_x: int) -> None:
        """NOT USED! Sets the maximum X coordinate (in sensor pixels/units) for the auto exposure ROI.

        Args:
            max_x (int): Maximum X for auto exposure region of interest.
        """
        ...
    def SetAcquisitionLineTime(self, line_time_us: int) -> None:
        """NOT USED! Sets the desired time per scan line (profile acquisition rate).

        Args:
            line_time_us (int): Time per line in microseconds.
        """
        ...
    def SetCameraMode(self, camera_images_mode: bool) -> None:
        """NOT USED! Sets the scanner to camera/image mode (if supported) instead of profile mode.

        Args:
            camera_images_mode (bool): True for camera mode, False for profile mode.
        """
        ...
    def SetUDPSocketPort(self, port: int) -> None:
        """NOT USED! Configures the UDP port for data transmission from the scanner.

        Args:
            port (int): The UDP port number.
        """
        ...
    def SetUDPSocketIP(self, ip_address: str) -> None:
        """NOT USED! Configures the destination IP address for UDP data transmission.

        Args:
            ip_address (str): The destination IP address.
        """
        ...
    def SetUDPSocketStart(self, start_transmission: bool) -> None:
        """NOT USED! Starts or stops UDP data transmission from the scanner.

        Args:
            start_transmission (bool): True to start, False to stop.
        """
        ...
    def SetHDR(self, enabled: bool) -> None:
        """NOT USED! Enables or disables High Dynamic Range (HDR) imaging mode.

        Args:
            enabled (bool): True to enable HDR, False to disable.
        """
        ...
    def SetExposureTime2(self, exposure_time_us: int) -> None:
        """NOT USED! Sets a secondary exposure time, often used in HDR mode.

        Args:
            exposure_time_us (int): Secondary exposure time in microseconds.
        """
        ...
    def SetRangeImageNrProfiles(self, num_profiles: int) -> None:
        """NOT USED! Sets the number of profiles to accumulate for a range image (if supported).

        Args:
            num_profiles (int): Number of profiles.
        """
        ...
    def SetRangeImageXScale(self, scale: float) -> None:
        """NOT USED! Sets the X-axis scaling factor for range image generation.

        Args:
            scale (float): Scaling factor.
        """
        ...
    def SetRangeImageXOffset(self, offset: float) -> None:
        """NOT USED! Sets the X-axis offset for range image generation.

        Args:
            offset (float): Offset value.
        """
        ...
    def SetRangeImageZScale(self, scale: float) -> None:
        """NOT USED! Sets the Z-axis scaling factor for range image generation.

        Args:
            scale (float): Scaling factor.
        """
        ...
    def SetRangeImageZOffset(self, offset: float) -> None:
        """NOT USED! Sets the Z-axis offset for range image generation.

        Args:
            offset (float): Offset value.
        """
        ...
    def SetLaserDeactivated(self, deactivated: bool) -> None:
        """NOT USED! Deactivates or activates the laser emitter.

        Args:
            deactivated (bool): True to deactivate the laser, False to activate.
        """
        ...
    def SetUserLED(self, led_mode: int) -> None:
        """NOT USED! Controls a user-configurable LED on the scanner.

        Args:
            led_mode (int): An integer code representing the LED state (e.g., 0=OFF, 1=ON, 2=BLINK).
        """
        ...
    def SetSignalContentZ(self, enabled: bool) -> None:
        """NOT USED! Enables or disables inclusion of Z (distance) data in the transmitted profile.

        Args:
            enabled (bool): True to include Z data, False otherwise.
        """
        ...
    def SetSignalContentStrength(self, enabled: bool) -> None:
        """NOT USED! Enables or disables inclusion of signal strength (intensity) data.

        Args:
            enabled (bool): True to include intensity data, False otherwise.
        """
        ...
    def SetSignalContentWidth(self, enabled: bool) -> None:
        """NOT USED! Enables or disables inclusion of signal width data.

        Args:
            enabled (bool): True to include signal width data, False otherwise.
        """
        ...
    def SetSignalContentReserved(self, enabled: bool) -> None:
        """NOT USED! Enables or disables inclusion of reserved signal content data.

        Args:
            enabled (bool): True to include, False otherwise.
        """
        ...
    def SetSocketConnectionTimeout(self, timeout_ms: int) -> None:
        """NOT USED! Sets the timeout for socket connection attempts.

        Args:
            timeout_ms (int): Timeout in milliseconds.
        """
        ...
    def SetHeartBeat(self, interval_ms: int) -> None:
        """NOT USED! Configures the heartbeat signal interval.

        Args:
            interval_ms (int): Heartbeat interval in milliseconds. 0 to disable.
        """
        ...
    def SetInitializeAcquisition(self) -> None:
        """NOT USED! Sends a command to initialize the acquisition hardware/software.

        Often required before starting acquisition.
        """
        ...
    def SetAcquisitionStart(self) -> None:
        """NOT USED! Sends a command to start data acquisition and transmission."""
        ...
    def SetAcquisitionStop(self) -> None:
        """NOT USED! Sends a command to stop data acquisition and transmission."""
        ...
    def SetResetSettings(self) -> None:
        """NOT USED! Resets scanner settings to factory defaults.

        Warning:
            This will erase current configuration.
        """
        ...
    def SetResetEncoder(self) -> None:
        """NOT USED! Resets the scanner's internal encoder counter."""
        ...
    def SetResetPictureCounter(self) -> None:
        """NOT USED! Resets the scanner's internal picture/profile counter."""
        ...
    def SetResetBaseTimeCounter(self) -> None:
        """NOT USED! Resets the scanner's internal base time counter."""
        ...
    def SetSettingsSave(self, set_index: int) -> None:
        """NOT USED! Saves the current scanner settings to a specified memory slot.

        Args:
            set_index (int): The index of the settings slot to save to.
        """
        ...
    def SetSettingsLoad(self, set_index: int) -> None:
        """NOT USED! Loads scanner settings from a specified memory slot.

        Args:
            set_index (int): The index of the settings slot to load from.
        """
        ...
    def SetTriggerSource(self, source_mode: int) -> None:
        """NOT USED! Sets the trigger source for profile acquisition.

        Args:
            source_mode (int): Integer code for trigger source (e.g., 0=Internal, 1=External, 2=Encoder).
        """
        ...
    def SetTriggerEncoderStep(self, step: int) -> None:
        """NOT USED! Sets the encoder step for encoder-based triggering.

        Acquires a profile every 'step' encoder ticks.

        Args:
            step (int): Encoder ticks per profile.
        """
        ...
    def SetTriggerDelay(self, delay_us: int) -> None:
        """NOT USED! Sets a delay after a trigger event before acquiring a profile.

        Args:
            delay_us (int): Delay in microseconds.
        """
        ...
    def SetTriggerSoftware(self) -> None:
        """NOT USED! Issues a software trigger for a single profile acquisition (if in software trigger mode)."""
        ...
    def SetEncoderTriggerFunction(self, function_mode: int) -> None:
        """NOT USED! Configures advanced encoder trigger functions.

        Args:
            function_mode (int): Integer code for the specific function.
        """
        ...
    def SetTriggerAmountProfilesY(self, mode: int) -> None: # 'Y' might refer to a batch or sequence
        """NOT USED! Sets the mode for acquiring a specific number of profiles per trigger.

        Args:
            mode (int): Integer code for the mode.
        """
        ...
    def SetAmountProfilesY(self, num_profiles: int) -> None:
        """NOT USED! Sets the number of profiles to acquire in a batch/sequence when triggered.

        Args:
            num_profiles (int): Number of profiles.
        """
        ...
    def SetSyncOut(self, duration_us: int) -> None:
        """NOT USED! Configures a synchronization output signal.

        Args:
            duration_us (int): Duration of the sync pulse in microseconds.
        """
        ...
    def SetSyncOutDelay(self, delay_us: int) -> None:
        """NOT USED! Sets a delay for the synchronization output signal.

        Args:
            delay_us (int): Delay in microseconds.
        """
        ...
    def SetSignalEnable(self, profile_selection: int) -> None: # Profile selection for signal processing
        """NOT USED! Enables or configures signal processing for selected profiles.

        Args:
            profile_selection (int): Integer code for profile selection criteria.
        """
        ...
    def SetSignalWidthMin(self, min_width: int) -> None:
        """NOT USED! Sets the minimum acceptable signal width for point validation.

        Args:
            min_width (int): Minimum signal width.
        """
        ...
    def SetSignalWidthMax(self, max_width: int) -> None:
        """NOT USED! Sets the maximum acceptable signal width for point validation.

        Args:
            max_width (int): Maximum signal width.
        """
        ...
    def SetSignalStrengthMin(self, min_strength: int) -> None:
        """NOT USED! Sets the minimum acceptable signal strength (intensity) for point validation.

        Args:
            min_strength (int): Minimum signal strength.
        """
        ...
    def SetSignalSelection(self, selection: int) -> None: # Selection criteria for valid signal
        """NOT USED! Sets advanced criteria for signal selection/validation.

        Args:
            selection (int): Integer code for selection criteria.
        """
        ...
    def SetLinearizationMode(self, enabled: bool) -> None:
        """NOT USED! Enables or disables linearization of scan data (if supported).

        Corrects for geometric distortions.

        Args:
            enabled (bool): True to enable linearization, False otherwise.
        """
        ...
    def SetEncoderCountDirection(self, inverted: bool) -> None:
        """NOT USED! Sets the counting direction for the encoder input.

        Args:
            inverted (bool): True to invert direction, False for normal.
        """
        ...
    def SetROI1WidthX(self, width: int) -> None:
        """NOT USED! Sets the width of Region of Interest 1 (ROI1) in X (pixels/sensor units).

        Args:
            width (int): Width of ROI1.
        """
        ...
    def SetROI1OffsetX(self, offset: int) -> None:
        """NOT USED! Sets the X offset of Region of Interest 1 (ROI1) (pixels/sensor units).

        Args:
            offset (int): X offset of ROI1.
        """
        ...
    def SetROI1StepX(self, step: int) -> None: # Subsampling step within ROI
        """NOT USED! Sets the X-axis subsampling step within ROI1.

        Args:
            step (int): Step value (e.g., 1 for every point, 2 for every other).
        """
        ...
    def SetROI1HeightZ(self, height: int) -> None:
        """NOT USED! Sets the height of Region of Interest 1 (ROI1) in Z (pixels/sensor units).

        Args:
            height (int): Height of ROI1.
        """
        ...
    def SetROI1OffsetZ(self, offset: int) -> None:
        """NOT USED! Sets the Z offset of Region of Interest 1 (ROI1) (pixels/sensor units).

        Args:
            offset (int): Z offset of ROI1.
        """
        ...
    def SetROI1StepZ(self, enabled: bool) -> None: # Z-axis step/subsampling enable for ROI1
        """NOT USED! Enables or disables Z-axis subsampling/stepping for ROI1.

        Args:
            enabled (bool): True to enable, False otherwise.
        """
        ...
    def SetROI1_mm(self, x1: float, z1: float, x2: float, z2: float) -> None:
        """NOT USED! Sets Region of Interest 1 (ROI1) using real-world millimeter coordinates.

        Defines a rectangular ROI.

        Args:
            x1 (float): Minimum X coordinate in mm.
            z1 (float): Minimum Z coordinate in mm.
            x2 (float): Maximum X coordinate in mm.
            z2 (float): Maximum Z coordinate in mm.
        """
        ...
    def SetROI1Z_mm(self, z1: float, z2: float) -> None:
        """NOT USED! Sets the Z-range of Region of Interest 1 (ROI1) using real-world millimeter coordinates.

        Args:
            z1 (float): Minimum Z coordinate in mm.
            z2 (float): Maximum Z coordinate in mm.
        """
        ...
    def SetEAFunction(self, ea_unit_number: int, function_code: int) -> None: # EA: External Axis/Access
        """NOT USED! Configures a function for an External Axis/Access (EA) unit.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            function_code (int): Integer code for the function to assign.
        """
        ...
    def SetEAFunctionLaserOff(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to control laser deactivation.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True if this EA unit controls laser off, False otherwise.
        """
        ...
    def SetEAFunctionProfileEnable(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to enable/disable profile acquisition.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True if this EA unit controls profile enable, False otherwise.
        """
        ...
    def SetEAFunctionResetCounter(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to reset a counter.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True if this EA unit controls counter reset, False otherwise.
        """
        ...
    def SetEAResetCounterRepeat(self, ea_unit_number: int, repeat_mode: int) -> None:
        """NOT USED! Sets the repeat mode for an EA-controlled counter reset.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            repeat_mode (int): Integer code for repeat mode.
        """
        ...
    def SetEAResetCounterSignaledge(self, ea_unit_number: int, edge_mode: int) -> None:
        """NOT USED! Sets the signal edge detection mode for an EA-controlled counter reset.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            edge_mode (int): Integer code for edge mode (e.g., rising, falling).
        """
        ...
    def SetEAResetCounterBaseTimeCounter(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to reset the base time counter.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True to enable this function for the EA unit.
        """
        ...
    def SetEAResetCounterPictureCounter(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to reset the picture/profile counter.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True to enable this function for the EA unit.
        """
        ...
    def SetEAResetCounterEncoderHTL(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to reset an HTL encoder counter.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True to enable this function for the EA unit.
        """
        ...
    def SetEAResetCounterEncoderTTLRS422(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to reset a TTL/RS422 encoder counter.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True to enable this function for the EA unit.
        """
        ...
    def SetEAInputFunction(self, ea_unit_number: int, active: bool) -> None: # 'active' might mean enable/disable the input
        """NOT USED! Configures the input function of an EA unit.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            active (bool): True to activate/enable the input function.
        """
        ...
    def SetEAInputLoad(self, ea_unit_number: int, enabled: bool) -> None: # e.g. pull-up/pull-down resistor
        """NOT USED! Configures input load (e.g., pull-up/pull-down) for an EA unit.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True to enable the load.
        """
        ...
    def SetEAOutput(self, ea_unit_number: int, output_mode: int) -> None:
        """NOT USED! Sets the output mode for an EA unit.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            output_mode (int): Integer code for the output mode.
        """
        ...
    def SetEAOutputFunction(self, ea_unit_number: int, normally_closed: bool) -> None:
        """NOT USED! Configures the output function of an EA unit (e.g., normally open/closed).

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            normally_closed (bool): True for normally closed, False for normally open.
        """
        ...
    def SetEAFunctionInputCounter(self, ea_unit_number: int, enabled: bool) -> None:
        """NOT USED! Configures an EA unit to act as an input counter.

        Args:
            ea_unit_number (int): Identifier for the EA unit.
            enabled (bool): True to enable input counter function.
        """
        ...
    def SetStatisticDataUserData(self, user_data: int) -> None:
        """NOT USED! Sets a user-defined data field to be included in statistics data.

        Args:
            user_data (int): Integer value for user data.
        """
        ...
    def SetLibraryScannerFiFoSize(self, fifo_size_bytes: int) -> None:
        """NOT USED! Sets the size of the FIFO buffer used by the client library for incoming scan data.

        Args:
            fifo_size_bytes (int): Size of the FIFO buffer in bytes.
        """
        ...
    def SetLibraryScannerFiFoMode(self, enabled: bool) -> None:
        """Enables or disables the client library's internal FIFO buffering for scan data.

        If enabled, `Receive()` might pull from this buffer. If disabled, `Receive()` might fetch directly.

        Args:
            enabled (bool): True to enable FIFO mode, False to disable.

        Examples:
        ```python
        # Off buffer
        l_client.SetLibraryScannerFiFoMode(False)
        ```
        """
        ...
    def SetAutoConnectMode(self, enabled: bool) -> None:
        """Enables or disables automatic reconnection attempts by the client library.

        If enabled, the client will try to re-establish connection if it's lost.

        Args:
            enabled (bool): True to enable auto-connect, False to disable.

        Examples:
        ```python
        # Assuming l_client is an initialized LaserClient
        l_client.SetAutoConnectMode(True)
        ```
        """
        ...
    def GetIP(self) -> str:
        """Gets the IP address the laser client is currently configured for.

        Returns:
            str: The IP address string.
        """
        ...
    def GetPort(self) -> str:
        """Gets the port (number or service name) the laser client is configured for.

        Returns:
            str: The port string.
        """
        ...

class WaamAPI:
    """Main class for the WAAM (Wire Arc Additive Manufacturing) API.

    Provides a high-level interface to interact with robot and laser scanner functionalities.
    Robot interaction can be with different coordinate frames (e.g., Base/World, Tool0-3).
    """
    thisown: property
    def __init__(self) -> None:
        """Constructor for WaamAPI.

        Initializes underlying clients (RobotClient, LaserClient) and other components.
        Settings are typically loaded from 'config.yaml'.

        Examples:
        ```python
        api = WaamAPI()
        # api.SetExecutablePriority() - it calls in WaamAPI()
        ```
        """
        ...
    def __swig_destroy__(self) -> None:
        """SWIG-managed destructor.

        Ensures all resources, clients, and threads are properly shut down.
        """
        ...
    def SetExecutablePriority(self) -> None:
        """Sets the priority of the current executable/process.

        Typically raises priority for real-time performance.
        Requires appropriate system permissions.
        """
        ...
    def ReadIO(self, command_str: str) -> "Response":
        """Sends a command to read I/O status from the robot and gets a response.

        The format of `command_str` is specific to the underlying robot controller protocol.
        Example: "1,1,10010,1,0,123" might represent a request to read a specific IO register.

        Args:
            command_str (str): The I/O read command string.

        Returns:
            "Response": A Response object containing the I/O status.

        Examples:
        ```python
        api = WaamAPI()
        io_response = api.ReadIO("1,1,10010,1,0,123") # Example command
        print(f"IO Response: {io_response.response_}")
        ```
        """
        ...
    def WriteIO(self, command_str: str) -> "Response":
        """Sends a command to write/set I/O status on the robot and gets a confirmation.

        Note:
            This method might be for lower-level access or specific scenarios.
            Prefer using dedicated methods like SetDOUT., if available for clarity.
            This method is reportedly not used in some typical workflows.

        Args:
            command_str (str): The I/O write command string.

        Returns:
            "Response": A Response object, typically confirming the action.
        """
        ...
    def ReadVariables(self, command_str: str) -> "Response":
        """Sends a command to read variabels from the robot and gets a response.

        The format of `command_str` is specific to the underlying robot controller protocol.
        Example: "1,1,2,1,0,123" read integer number 1.

        Args:
            command_str (str): The variable read command string.

        Returns:
            "Response": A Response object containing the variabels.

        Examples:
        ```python
        api = WaamAPI()
        var_response = api.ReadVariables("1,1,2,1,0,123") # Example command
        print(f"IO Response: {var_response.response_}")
        ```
        """
        ...
    def WriteVariables(self, command_str: str) -> "Response":
        """Sends a command to write variabels on the robot and gets a confirmation.

        Note:
            This method might be for lower-level access or specific scenarios.
            Prefer using dedicated methods like SetByte, SetInteger and etc., if available for clarity.
            This method is reportedly not used in some typical workflows.

        Args:
            command_str (str): The variabels write command string.

        Returns:
            "Response": A Response object, typically confirming the action.
        """
        ...
    def ReadCoordinate(self, command_str: str) -> "Response":
        """Sends a command to read coordinate data from the robot.

        The command string determines the coordinate frame and type of data.
        Example: "10,1,3,1" might request current coordinates in a specific user frame. Base frame Tool 3.

        Args:
            command_str (str): The coordinate read command string.

        Returns:
            "Response": A Response object containing the raw coordinate data string.

        Examples:
        ```python
        api = WaamAPI()
        coord_response = api.ReadCoordinate("10,1,3,1") # Example command
        print(f"Coord Response: {coord_response.response_}")
        # Further parsing of coord_response.response_ would be needed
        ```
        """
        ...
    def ReadCoordinate(self, frame: int, tool: int) -> "Response":
        """Sends a command to read coordinate data from the robot.

        The command take frame and tool numbers.
        Example: "ReadCoordinate(2,3)" meanse User frame 1 and Tool 3.

        Args:
            frame (int): The frame number.
            tool (int): The tool number.
        Returns:
            "Response": A Response object containing the raw coordinate data string.

        Examples:
        ```python
        api = WaamAPI()
        coord_response = api.ReadCoordinate(FRAME_USER1, TOOL_3) # Example command
        print(f"Coord Response: {coord_response.response_}")
        # Further parsing of coord_response.response_ would be needed
        ```
        """
        ...
    def ReadBase0(self) -> "Coordinate":
        """Reads the robot's coordinates relative to Base 0 (World frame).

        Returns:
            "Coordinate": A Coordinate object.

        Examples:
        ```python
        api = WaamAPI()
        coord = api.ReadBase0()
        print(f"Base0: X={coord.x}, Y={coord.y}, Z={coord.z}")
        ```
        """
        ...
    def ScannerBase0(self) -> "CoordinateScan":
        """Gets a CoordinateScan object for continuously scanning robot coordinates in Base 0 (World frame).

        Returns:
            "CoordinateScan": A CoordinateScan instance for Base 0.

        Examples:
        ```python
        api = WaamAPI()
        scanner = api.ScannerBase0()
        scanner.Start()
        for _ in range(2): # Get 2 new data points
            while not scanner.IsNew():
                pass # Wait for new data (in a real app, use time.sleep or async)
            data = scanner.Get()
            print(f"Scanned Base0 X: {data.x}")
        scanner.Stop()
        scanner.Destroy()
        ```
        """
        ...
    def ReadBase3(self) -> "Coordinate":
        """Reads the robot's coordinates relative to Base 3 (Base frame Tool 3).

        Returns:
            "Coordinate": A Coordinate object.

        Examples:
        ```python
        api = WaamAPI()
        coord = api.ReadBase3()
        print(f"Base3: X={coord.x}, Y={coord.y}, Z={coord.z}")
        ```
        """
        ...
    def ScannerBase3(self) -> "CoordinateScan":
        """Gets a CoordinateScan object for continuously scanning robot coordinates in Base 3 (Base frame Tool 3).

        Returns:
            "CoordinateScan": A CoordinateScan instance for Base 3.

        Examples:
        ```python
        api = WaamAPI()
        scanner = api.ScannerBase3()
        scanner.Start()
        for _ in range(2):
            while not scanner.IsNew():
                pass
            data = scanner.Get()
            print(f"Scanned Base3 X: {data.x}")
        scanner.Stop()
        scanner.Destroy()
        ```
        """
        ...
    def ReadWeldParametrs(self) -> "WeldParametrs":
        r"""Reads the current welding parameters from the WaamAPI.

        This method queries the underlying system, likely via _PyWaamAPI,
        to obtain the latest welding parameters such as current, voltage,
        wire feed speed, and welding status.

        Returns:
            WeldParametrs: An object populated with the current welding parameters.
        """
        ... 
    def ReadJobParametrs(self) -> "JobParametrs":
        r"""Reads the current job parameters and status from the WaamAPI.

        This method queries the underlying system, likely via _PyWaamAPI,
        to obtain details about the currently active or selected job,
        including its name, execution line, step, operational state (hold/work),
        and active frame/tool.

        Returns:
            JobParametrs: An object populated with the current job parameters and status.
        """
        ... 
    def GetDOUT(self, pin_id: int, duration_ms: int = 100) -> bool:
        """Gets the state of a specific digital output pin.

        Args:
            pin_id (int): The ID/index of the DOUT pin.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Returns:
            bool: True if the pin is ON, False if OFF.

        Examples:
        ```python
        api = WaamAPI()
        state = api.GetDOUT(1)
        print(f"DOUT 1 is {'ON' if state else 'OFF'}")
        ```
        """
        ...
    def SetDOUT(self, pin_id: int, state: bool, duration_ms: int = 100) -> None:
        """Sets the state of a specific digital output pin.

        Example: `SetDOUT(1, True)` means set `DOUT1=ON`.

        Args:
            pin_id (int): The ID/index of the DOUT pin.
            state (bool): The desired state (True for ON, False for OFF).
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Examples:
        ```python
        api = WaamAPI()
        api.SetDOUT(1, True) # Sets DOUT1=ON
        current_state = api.GetDOUT(1)
        print(f"DOUT 1 state after SetDOUT: {current_state}")
        ```
        """
        ...
    def WaitDOUT(self, pin_id: int, state: bool, duration_ms: int = 100) -> None:
        """Waits until a specific digital output pin reaches the desired state, or timeout occurs.

        Example: `WaitDOUT(1, True)` waits for `DOUT1=ON`.
        The `duration_ms` here is the timeout for waiting, plus a final reliability delay.

        Args:
            pin_id (int): The ID/index of the DOUT pin.
            state (bool): The desired state to wait for (True for ON, False for OFF).
            duration_ms (int): Time to wait. Defaults to 100ms.

        Note:
            This is a blocking call.

        Examples:
        ```python
        api = WaamAPI()
        # Assuming DOUT 1 is currently OFF
        api.SetDOUT(1, True) # Command to turn ON
        api.WaitDOUT(1, True, 500) # Wait 500 ms and after check again
        print("DOUT 1 is now ON")
        ```
        """
        ...
    def GetByte(self, pin_id: int, duration_ms: int = 100) -> int:
        """Gets the value of a byte-type variable associated with `pin_id`.

        Note: The term `pin_id` might refer to a variable identifier in this context.
        The underlying command protocol might resemble "1,1,1,pin_id,..."

        Args:
            pin_id (int): The ID/index of the byte variable.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Returns:
            int: The byte value (0-255).

        Examples:
        ```python
        api = WaamAPI()
        val = api.GetByte(10) # Get byte variable with ID 10
        print(f"Byte var 10: {val}")
        ```
        """
        ...
    def GetInteger(self, pin_id: int, duration_ms: int = 100) -> int:
        """Gets the value of an integer-type variable associated with `pin_id`.

        Note: The term `pin_id` might refer to a variable identifier.
        The underlying command protocol might resemble "1,1,2,pin_id,..."

        Args:
            pin_id (int): The ID/index of the integer variable.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Returns:
            int: The integer value.

        Examples:
        ```python
        api = WaamAPI()
        val = api.GetInteger(10) # Get integer variable with ID 10
        print(f"Int var 10: {val}")
        ```
        """
        ...
    def GetDouble(self, pin_id: int, duration_ms: int = 100) -> int:
        """Gets the value of a double-type variable associated with `pin_id`, returned as an integer.

        The C++ implementation might return an int (e.g., scaled or truncated representation of a double).
        Note: The term `pin_id` might refer to a variable identifier.
        The underlying command protocol might resemble "1,1,3,pin_id,..."

        Args:
            pin_id (int): The ID/index of the double variable.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Returns:
            int: The integer representation of the double value.
        """
        ...
    def GetBytes(self, pins_id: IntVector, duration_ms: int = 100) -> MapUIntInt:
        """Gets the values of multiple byte-type variables.

        Args:
            pins_id (IntVector): A vector of IDs/indices for the byte variables.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Returns:
            MapUIntInt: A map where keys are variable IDs and values are their byte values.

        Examples:
        ```python
        api = WaamAPI()
        ids = IntVector([10, 11])
        byte_map = api.GetBytes(ids)
        for pin_id in byte_map:
            print(f"Byte var {pin_id}: {byte_map[pin_id]}")
        ```
        """
        ...
    def GetIntegers(self, pins_id: IntVector, duration_ms: int = 100) -> MapUIntInt:
        """Gets the values of multiple integer-type variables.

        Args:
            pins_id (IntVector): A vector of IDs/indices for the integer variables.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Returns:
            MapUIntInt: A map where keys are variable IDs and values are their integer values.

        Examples:
        ```python
        api = WaamAPI()
        ids = IntVector([10, 11])
        int_map = api.GetIntegers(ids)
        for pin_id in int_map:
            print(f"Int var {pin_id}: {int_map[pin_id]}")
        ```
        """
        ...
    def GetDoubles(self, pins_id: IntVector, duration_ms: int = 100) -> MapUIntInt:
        """Gets the values of multiple double-type variables, with values returned as integers.

        The C++ implementation might return int values (e.g., scaled or truncated representations of doubles)
        within the MapUIntInt structure.

        Args:
            pins_id (IntVector): A vector of IDs/indices for the double variables.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Returns:
            MapUIntInt: A map where keys are variable IDs and values are their integer representations
                        of the double values.
        """
        ...
    def SetByte(self, pin_id: int, value: int, duration_ms: int = 100) -> None:
        """Sets the value of a byte-type variable associated with `pin_id`.

        Note: The term `pin_id` might refer to a variable identifier.

        Args:
            pin_id (int): The ID/index of the byte variable.
            value (int): The byte value to set (0-255).
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Examples:
        ```python
        api = WaamAPI()
        api.SetByte(10, 255) # Set byte variable 10 to 255
        ```
        """
        ...
    def SetInteger(self, pin_id: int, value: int, duration_ms: int = 100) -> None:
        """Sets the value of an integer-type variable associated with `pin_id`.

        Note: The term `pin_id` might refer to a variable identifier.

        Args:
            pin_id (int): The ID/index of the integer variable.
            value (int): The integer value to set.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Examples:
        ```python
        api = WaamAPI()
        api.SetInteger(10, 12345) # Set int variable 10 to 12345
        ```
        """
        ...
    def SetDouble(self, pin_id: int, value: int, duration_ms: int = 100) -> None:
        """Sets the value of a double-type variable associated with `pin_id`, accepting an integer.

        The C++ implementation might expect an int (e.g., for scaled or specific representation of a double).
        Note: The term `pin_id` might refer to a variable identifier.

        Args:
            pin_id (int): The ID/index of the double variable.
            value (int): The integer representation of the double value to set.
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100ms.

        Examples:
        ```python
        api = WaamAPI()
        api.SetDouble(10, 12345) # Set double variable 10 (as int)
        ```
        """
        ...
    @overload
    def GetDOUTRange(self, from_pin: int, to_pin: int, duration_ms: int = 100) -> MapUIntBool: ...
    @overload
    def GetDOUTRange(self, pins_id: IntVector, duration_ms: int = 100) -> MapUIntBool: ...
    def GetDOUTRange(self, *args: Any) -> MapUIntBool:
        """Gets the states of a range of digital output pins.

        Can be called with a start/end pin ID or a vector of pin IDs.

        Args:
            from_pin (int, optional): Starting pin ID (if using range).
            to_pin (int, optional): Ending pin ID (if using range).
            pins_id (IntVector, optional): A vector of pin IDs (if using list).
            duration_ms (int): Delay at the end of the method for reliability. Defaults to 100.

        Returns:
            MapUIntBool: A map where keys are pin IDs and values are their boolean states.

        Examples:
        ```python
        api = WaamAPI()
        # Overload 1: from, to
        dout_map1 = api.GetDOUTRange(1, 3)
        for pin_id in dout_map1:
            print(f"DOUT {pin_id} (range): {dout_map1[pin_id]}")

        # Overload 2: vector of pins
        id_vec = IntVector([5, 6])
        dout_map2 = api.GetDOUTRange(id_vec)
        for pin_id in dout_map2:
            print(f"DOUT {pin_id} (vector): {dout_map2[pin_id]}")
        ```
        """
        ... # Implementation for overload
    def ReadLaser(self) -> "LaserCoordinate": # Removed clean_buf_flag based on original Python file
        """Reads a single processed laser scan (profile).

        This typically involves triggering the laser, receiving raw data, and filtering it.

        Returns:
            "LaserCoordinate": A LaserCoordinate object containing the processed scan data.

        Examples:
        ```python
        api = WaamAPI()
        laser_scan = api.ReadLaser()
        print(f"Laser scan ID: {laser_scan.id}, Points: {len(laser_scan.x)}")
        ```
        """
        ...
    def ScannerLaser(self) -> "LaserCoordinateScan":
        """Gets a LaserCoordinateScan object for continuously scanning processed laser data.

        Returns:
            "LaserCoordinateScan": A LaserCoordinateScan instance.

        Examples:
        ```python
        api = WaamAPI()
        scanner = api.ScannerLaser()
        scanner.Start()
        for _ in range(2):
            while not scanner.IsNew():
                pass
            data = scanner.Get()
            print(f"Scanned Laser ID: {data.id}, Points: {len(data.x)}")
        scanner.Stop()
        scanner.Destroy()
        ```
        """
        ...
    def ReadLaserBase0(self) -> "RobotLaserCoordinate":
        """Reads combined robot coordinates (Base 0 - World frame Tool 0) and a laser scan.

        Synchronizes robot position reading with a laser scan.

        Returns:
            "RobotLaserCoordinate": A RobotLaserCoordinate object.

        Examples:
        ```python
        api = WaamAPI()
        combined_data = api.ReadLaserBase0()
        print(f"Robot X (Base0): {combined_data.x}, Laser Points: {len(combined_data.x_arr)}")
        ```
        """
        ...
    def ScannerLaserBase0(self) -> "RobotLaserCoordinateScan":
        """Gets a scanner for continuous acquisition of combined robot (Base 0 - World frame Tool 0) and laser data.

        Returns:
            "RobotLaserCoordinateScan": A RobotLaserCoordinateScan instance for Base 0.

        Examples:
        ```python
        api = WaamAPI()
        scanner = api.ScannerLaserBase0()
        scanner.Start()
        for _ in range(2):
            while not scanner.IsNew():
                pass
            data = scanner.Get()
            print(f"Scanned R+L (Base0) X: {data.x}, Laser Points: {len(data.x_arr)}")
        scanner.Stop()
        scanner.Destroy()
        ```
        """
        ...
    def ReadLaserBase3(self) -> "RobotLaserCoordinate":
        """Reads combined robot coordinates (Base 3 - User frame Tool 3) and a laser scan.

        Returns:
            "RobotLaserCoordinate": A RobotLaserCoordinate object.

        Examples:
        ```python
        api = WaamAPI()
        combined_data = api.ReadLaserBase3()
        print(f"Robot X (Base3): {combined_data.x}, Laser Points: {len(combined_data.x_arr)}")
        ```
        """
        ...
    def ScannerLaserBase3(self, period: int = 50, is_save: bool = True) -> "RobotLaserCoordinateScan":
        """Gets a scanner for continuous acquisition of combined robot (Base 3 - User frame Tool 3) and laser data.

        Args:
            period (int): Scanning period in milliseconds. Defaults to 50.
            is_save (bool): Whether to save scanned data to CSV. Defaults to True.

        Returns:
            "RobotLaserCoordinateScan": A RobotLaserCoordinateScan instance for Base 3.

        Examples:
        ```python
        api = WaamAPI()
        scanner = api.ScannerLaserBase3(period=100, is_save=False)
        scanner.Start()
        for _ in range(2):
            while not scanner.IsNew():
                pass
            data = scanner.Get()
            print(f"Scanned R+L (Base3) X: {data.x}, Laser Points: {len(data.x_arr)}")
        scanner.Stop()
        scanner.Destroy()
        ```
        """
        ...
    def ScannerLaserBase3ByDOUT1(self, period: int = 10) -> None:
        """Starts a continuous scanning process for combined robot (Base 3 - User frame Tool 3) and laser data.

        Scanning is triggered and controlled by Digital Output Pin 1 (DOUT1).
        Multiple scans occur at the specified `period` while DOUT1=ON.
        The scanner pauses when DOUT1=OFF and resumes when DOUT1=ON again.

        Args:
            period (int): Scanning period in milliseconds after DOUT1=ON trigger. Defaults to 10 ms.

        Note:
            This method initiates an asynchronous scanning process. Data retrieval mechanisms
            depend on the API's specific implementation.

        Examples:
        ```python
        api = WaamAPI()
        api.ScannerLaserBase3ByDOUT1(period=20)
        ```
        """
        ...
    def ReadLaserBase3ByDOUT1(self) -> None:
        """Performs a single laser scan in Base 3 (User frame Tool 3) coordinated with DOUT1.

        This action is triggered when DOUT1=ON. After the scan, this function sets DOUT1=OFF.
        The system then waits for a signal from the robot (presumably the robot setting DOUT1=ON again)
        before this function can be successfully called for another single scan.

        Note:
            The `None` return type suggests this method primarily performs an action.
            Data might be available via other methods or internal buffers.

        Examples:
        ```python
        api = WaamAPI()
        api.ReadLaserBase3ByDOUT1() # Performs one scan if DOUT1=ON, then sets DOUT1=OFF
        ```
        """
        ...
    def ScannerLaserBase0ByDOUT1(self, period: int = 10) -> None:
        """Starts a continuous scanning process for combined robot (Base 0 - World frame Tool 0) and laser data.

        Triggered and controlled by Digital Output Pin 1 (DOUT1).
        Scanning occurs (multiple scans at the specified `period`) while DOUT1=ON.
        The scanner pauses when DOUT1=OFF and resumes when DOUT1=ON again.

        Args:
            period (int): Scanning period in milliseconds after DOUT1=ON trigger. Defaults to 10 ms.

        Examples:
        ```python
        api = WaamAPI()
        api.ScannerLaserBase0ByDOUT1(period=25)
        ```
        """
        ...
    def ReadLaserBase0ByDOUT1(self) -> None:
        """Performs a single laser scan in Base 0 (World frame Tool 0) coordinated with DOUT1.

        This action is triggered when DOUT1=ON. After the scan, this function sets DOUT1=OFF.
        The system then waits for a signal from the robot (presumably the robot setting DOUT1=ON again)
        before this function can be successfully called for another single scan.

        Note:
            See notes for `ReadLaserBase3ByDOUT1` regarding data retrieval.

        Examples:
        ```python
        api = WaamAPI()
        api.ReadLaserBase0ByDOUT1()
        ```
        """
        ...
    def ReadBase0ByDOUT1(self) -> None:
        """Performs a single laser scan in Base 0 (World frame Tool 0) coordinated with DOUT1.

        This action is triggered when DOUT1=ON. After the scan, this function sets DOUT1=OFF.
        The system then waits for a signal from the robot (presumably the robot setting DOUT1=ON again)
        before this function can be successfully called for another single scan.

        Note:
            See notes for `ReadLaserBase0ByDOUT1` regarding data retrieval.

        Examples:
        ```python
        api = WaamAPI()
        api.ReadBase0ByDOUT1()
        ```
        """
        ...
        
    def SetReadCount(self, read_count: int) -> None:
        """Set read count, it is like a trigger for new file creation.    waam_.SetReadCount(4);
        Examples:
        ```python
        api = WaamAPI()
        api.SetReadCount(4)
        api.ReadBase0ByDOUT1()
        ```
        """
        ...
    def SetMaxCount(self, read_count: int) -> None:
        """Not used. Implimentation in progress
        """
        ...
    
    def ExtractRobotLaserCSV(self, path: str = "") -> "List[List[RobotLaserCoordinate]]":
        """Extracts RobotLaserCoordinate data from a CSV file.

        Args:
            path (str): The path to the CSV file. If empty, uses the default path. Defaults to "".

        Returns:
            VectorVectorRobotLaserCoordinate: A vector of vectors, where each inner vector
                                              represents a sequence of RobotLaserCoordinate data.
        """
        ...
    
    def ExtractRobotCSV(self, path: str = "") -> "List[List[Coordinate]]":
        """Extracts Coordinate data from a CSV file.

        Args:
            path (str): The path to the CSV file. If empty, uses the default path. Defaults to "".

        Returns:
            VectorVectorCoordinate: A vector of vectors, where each inner vector
                                              represents a sequence of Coordinate data.
        """
        ...
    
    def ExtractLaserCSV(self, path: str = "") -> "List[List[LaserCoordinate]]":
        """Extracts LaserCoordinate data from a CSV file.

        Args:
            path (str): The path to the CSV file. If empty, uses the default path. Defaults to "".

        Returns:
            VectorVectorLaserCoordinate: A vector of vectors, where each inner vector
                                              represents a sequence of LaserCoordinate data.
        """
        ...
