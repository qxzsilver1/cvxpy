# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _cvxcore
else:
    import _cvxcore

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cvxcore.delete_SwigPyIterator

    def value(self) -> "PyObject *":
        return _cvxcore.SwigPyIterator_value(self)

    def incr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _cvxcore.SwigPyIterator_incr(self, n)

    def decr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _cvxcore.SwigPyIterator_decr(self, n)

    def distance(self, x: "SwigPyIterator") -> "ptrdiff_t":
        return _cvxcore.SwigPyIterator_distance(self, x)

    def equal(self, x: "SwigPyIterator") -> "bool":
        return _cvxcore.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _cvxcore.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _cvxcore.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _cvxcore.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _cvxcore.SwigPyIterator_previous(self)

    def advance(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _cvxcore.SwigPyIterator_advance(self, n)

    def __eq__(self, x: "SwigPyIterator") -> "bool":
        return _cvxcore.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: "SwigPyIterator") -> "bool":
        return _cvxcore.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _cvxcore.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _cvxcore.SwigPyIterator___isub__(self, n)

    def __add__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _cvxcore.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _cvxcore.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _cvxcore:
_cvxcore.SwigPyIterator_swigregister(SwigPyIterator)

VARIABLE = _cvxcore.VARIABLE
PARAM = _cvxcore.PARAM
PROMOTE = _cvxcore.PROMOTE
MUL = _cvxcore.MUL
RMUL = _cvxcore.RMUL
MUL_ELEM = _cvxcore.MUL_ELEM
DIV = _cvxcore.DIV
SUM = _cvxcore.SUM
NEG = _cvxcore.NEG
INDEX = _cvxcore.INDEX
TRANSPOSE = _cvxcore.TRANSPOSE
SUM_ENTRIES = _cvxcore.SUM_ENTRIES
TRACE = _cvxcore.TRACE
RESHAPE = _cvxcore.RESHAPE
DIAG_VEC = _cvxcore.DIAG_VEC
DIAG_MAT = _cvxcore.DIAG_MAT
UPPER_TRI = _cvxcore.UPPER_TRI
CONV = _cvxcore.CONV
HSTACK = _cvxcore.HSTACK
VSTACK = _cvxcore.VSTACK
SCALAR_CONST = _cvxcore.SCALAR_CONST
DENSE_CONST = _cvxcore.DENSE_CONST
SPARSE_CONST = _cvxcore.SPARSE_CONST
NO_OP = _cvxcore.NO_OP
KRON = _cvxcore.KRON
class LinOp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    type = property(_cvxcore.LinOp_type_get, _cvxcore.LinOp_type_set)
    size = property(_cvxcore.LinOp_size_get, _cvxcore.LinOp_size_set)
    args = property(_cvxcore.LinOp_args_get, _cvxcore.LinOp_args_set)
    linOp_data = property(_cvxcore.LinOp_linOp_data_get, _cvxcore.LinOp_linOp_data_set)
    data_ndim = property(_cvxcore.LinOp_data_ndim_get, _cvxcore.LinOp_data_ndim_set)
    sparse = property(_cvxcore.LinOp_sparse_get, _cvxcore.LinOp_sparse_set)
    sparse_data = property(_cvxcore.LinOp_sparse_data_get, _cvxcore.LinOp_sparse_data_set)
    dense_data = property(_cvxcore.LinOp_dense_data_get, _cvxcore.LinOp_dense_data_set)
    slice = property(_cvxcore.LinOp_slice_get, _cvxcore.LinOp_slice_set)

    def __init__(self):
        _cvxcore.LinOp_swiginit(self, _cvxcore.new_LinOp())

    def has_constant_type(self) -> "bool":
        return _cvxcore.LinOp_has_constant_type(self)

    def set_linOp_data(self, tree: "LinOp") -> "void":
        return _cvxcore.LinOp_set_linOp_data(self, tree)

    def set_dense_data(self, matrix: "double *") -> "void":
        return _cvxcore.LinOp_set_dense_data(self, matrix)

    def set_sparse_data(self, data: "double *", row_idxs: "double *", col_idxs: "double *", rows: "int", cols: "int") -> "void":
        return _cvxcore.LinOp_set_sparse_data(self, data, row_idxs, col_idxs, rows, cols)
    __swig_destroy__ = _cvxcore.delete_LinOp

# Register LinOp in _cvxcore:
_cvxcore.LinOp_swigregister(LinOp)


def vecprod(vec: "IntVector") -> "int":
    return _cvxcore.vecprod(vec)

def vecprod_before(vec: "IntVector", end: "int") -> "int":
    return _cvxcore.vecprod_before(vec, end)

def tensor_mul(lh_ten: "Tensor const &", rh_ten: "Tensor const &") -> "Tensor":
    return _cvxcore.tensor_mul(lh_ten, rh_ten)

def acc_tensor(lh_ten: "Tensor &", rh_ten: "Tensor const &") -> "void":
    return _cvxcore.acc_tensor(lh_ten, rh_ten)

def diagonalize(mat: "Matrix const &") -> "Matrix":
    return _cvxcore.diagonalize(mat)
class ProblemData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    TensorV = property(_cvxcore.ProblemData_TensorV_get, _cvxcore.ProblemData_TensorV_set)
    TensorI = property(_cvxcore.ProblemData_TensorI_get, _cvxcore.ProblemData_TensorI_set)
    TensorJ = property(_cvxcore.ProblemData_TensorJ_get, _cvxcore.ProblemData_TensorJ_set)
    param_id = property(_cvxcore.ProblemData_param_id_get, _cvxcore.ProblemData_param_id_set)
    vec_idx = property(_cvxcore.ProblemData_vec_idx_get, _cvxcore.ProblemData_vec_idx_set)

    def init_id(self, new_param_id: "int", param_size: "int") -> "void":
        return _cvxcore.ProblemData_init_id(self, new_param_id, param_size)

    def getLen(self) -> "int":
        return _cvxcore.ProblemData_getLen(self)

    def getV(self, values: "double *") -> "void":
        return _cvxcore.ProblemData_getV(self, values)

    def getI(self, values: "double *") -> "void":
        return _cvxcore.ProblemData_getI(self, values)

    def getJ(self, values: "double *") -> "void":
        return _cvxcore.ProblemData_getJ(self, values)

    def __init__(self):
        _cvxcore.ProblemData_swiginit(self, _cvxcore.new_ProblemData())
    __swig_destroy__ = _cvxcore.delete_ProblemData

# Register ProblemData in _cvxcore:
_cvxcore.ProblemData_swigregister(ProblemData)
cvar = _cvxcore.cvar
CONSTANT_ID = cvar.CONSTANT_ID

class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _cvxcore.IntVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _cvxcore.IntVector___bool__(self)

    def __len__(self) -> "std::vector< int >::size_type":
        return _cvxcore.IntVector___len__(self)

    def __getslice__(self, i: "std::vector< int >::difference_type", j: "std::vector< int >::difference_type") -> "std::vector< int,std::allocator< int > > *":
        return _cvxcore.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _cvxcore.IntVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< int >::difference_type", j: "std::vector< int >::difference_type") -> "void":
        return _cvxcore.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _cvxcore.IntVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< int >::value_type const &":
        return _cvxcore.IntVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _cvxcore.IntVector___setitem__(self, *args)

    def pop(self) -> "std::vector< int >::value_type":
        return _cvxcore.IntVector_pop(self)

    def append(self, x: "std::vector< int >::value_type const &") -> "void":
        return _cvxcore.IntVector_append(self, x)

    def empty(self) -> "bool":
        return _cvxcore.IntVector_empty(self)

    def size(self) -> "std::vector< int >::size_type":
        return _cvxcore.IntVector_size(self)

    def swap(self, v: "IntVector") -> "void":
        return _cvxcore.IntVector_swap(self, v)

    def begin(self) -> "std::vector< int >::iterator":
        return _cvxcore.IntVector_begin(self)

    def end(self) -> "std::vector< int >::iterator":
        return _cvxcore.IntVector_end(self)

    def rbegin(self) -> "std::vector< int >::reverse_iterator":
        return _cvxcore.IntVector_rbegin(self)

    def rend(self) -> "std::vector< int >::reverse_iterator":
        return _cvxcore.IntVector_rend(self)

    def clear(self) -> "void":
        return _cvxcore.IntVector_clear(self)

    def get_allocator(self) -> "std::vector< int >::allocator_type":
        return _cvxcore.IntVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _cvxcore.IntVector_pop_back(self)

    def erase(self, *args) -> "std::vector< int >::iterator":
        return _cvxcore.IntVector_erase(self, *args)

    def __init__(self, *args):
        _cvxcore.IntVector_swiginit(self, _cvxcore.new_IntVector(*args))

    def push_back(self, x: "std::vector< int >::value_type const &") -> "void":
        return _cvxcore.IntVector_push_back(self, x)

    def front(self) -> "std::vector< int >::value_type const &":
        return _cvxcore.IntVector_front(self)

    def back(self) -> "std::vector< int >::value_type const &":
        return _cvxcore.IntVector_back(self)

    def assign(self, n: "std::vector< int >::size_type", x: "std::vector< int >::value_type const &") -> "void":
        return _cvxcore.IntVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _cvxcore.IntVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _cvxcore.IntVector_insert(self, *args)

    def reserve(self, n: "std::vector< int >::size_type") -> "void":
        return _cvxcore.IntVector_reserve(self, n)

    def capacity(self) -> "std::vector< int >::size_type":
        return _cvxcore.IntVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_IntVector

# Register IntVector in _cvxcore:
_cvxcore.IntVector_swigregister(IntVector)

class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _cvxcore.DoubleVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _cvxcore.DoubleVector___bool__(self)

    def __len__(self) -> "std::vector< double >::size_type":
        return _cvxcore.DoubleVector___len__(self)

    def __getslice__(self, i: "std::vector< double >::difference_type", j: "std::vector< double >::difference_type") -> "std::vector< double,std::allocator< double > > *":
        return _cvxcore.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _cvxcore.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< double >::difference_type", j: "std::vector< double >::difference_type") -> "void":
        return _cvxcore.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _cvxcore.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< double >::value_type const &":
        return _cvxcore.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _cvxcore.DoubleVector___setitem__(self, *args)

    def pop(self) -> "std::vector< double >::value_type":
        return _cvxcore.DoubleVector_pop(self)

    def append(self, x: "std::vector< double >::value_type const &") -> "void":
        return _cvxcore.DoubleVector_append(self, x)

    def empty(self) -> "bool":
        return _cvxcore.DoubleVector_empty(self)

    def size(self) -> "std::vector< double >::size_type":
        return _cvxcore.DoubleVector_size(self)

    def swap(self, v: "DoubleVector") -> "void":
        return _cvxcore.DoubleVector_swap(self, v)

    def begin(self) -> "std::vector< double >::iterator":
        return _cvxcore.DoubleVector_begin(self)

    def end(self) -> "std::vector< double >::iterator":
        return _cvxcore.DoubleVector_end(self)

    def rbegin(self) -> "std::vector< double >::reverse_iterator":
        return _cvxcore.DoubleVector_rbegin(self)

    def rend(self) -> "std::vector< double >::reverse_iterator":
        return _cvxcore.DoubleVector_rend(self)

    def clear(self) -> "void":
        return _cvxcore.DoubleVector_clear(self)

    def get_allocator(self) -> "std::vector< double >::allocator_type":
        return _cvxcore.DoubleVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _cvxcore.DoubleVector_pop_back(self)

    def erase(self, *args) -> "std::vector< double >::iterator":
        return _cvxcore.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _cvxcore.DoubleVector_swiginit(self, _cvxcore.new_DoubleVector(*args))

    def push_back(self, x: "std::vector< double >::value_type const &") -> "void":
        return _cvxcore.DoubleVector_push_back(self, x)

    def front(self) -> "std::vector< double >::value_type const &":
        return _cvxcore.DoubleVector_front(self)

    def back(self) -> "std::vector< double >::value_type const &":
        return _cvxcore.DoubleVector_back(self)

    def assign(self, n: "std::vector< double >::size_type", x: "std::vector< double >::value_type const &") -> "void":
        return _cvxcore.DoubleVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _cvxcore.DoubleVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _cvxcore.DoubleVector_insert(self, *args)

    def reserve(self, n: "std::vector< double >::size_type") -> "void":
        return _cvxcore.DoubleVector_reserve(self, n)

    def capacity(self) -> "std::vector< double >::size_type":
        return _cvxcore.DoubleVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_DoubleVector

# Register DoubleVector in _cvxcore:
_cvxcore.DoubleVector_swigregister(DoubleVector)

class IntVector2D(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.IntVector2D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _cvxcore.IntVector2D___nonzero__(self)

    def __bool__(self) -> "bool":
        return _cvxcore.IntVector2D___bool__(self)

    def __len__(self) -> "std::vector< std::vector< int > >::size_type":
        return _cvxcore.IntVector2D___len__(self)

    def __getslice__(self, i: "std::vector< std::vector< int > >::difference_type", j: "std::vector< std::vector< int > >::difference_type") -> "std::vector< std::vector< int,std::allocator< int > >,std::allocator< std::vector< int,std::allocator< int > > > > *":
        return _cvxcore.IntVector2D___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _cvxcore.IntVector2D___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< std::vector< int > >::difference_type", j: "std::vector< std::vector< int > >::difference_type") -> "void":
        return _cvxcore.IntVector2D___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _cvxcore.IntVector2D___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< std::vector< int > >::value_type const &":
        return _cvxcore.IntVector2D___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _cvxcore.IntVector2D___setitem__(self, *args)

    def pop(self) -> "std::vector< std::vector< int > >::value_type":
        return _cvxcore.IntVector2D_pop(self)

    def append(self, x: "IntVector") -> "void":
        return _cvxcore.IntVector2D_append(self, x)

    def empty(self) -> "bool":
        return _cvxcore.IntVector2D_empty(self)

    def size(self) -> "std::vector< std::vector< int > >::size_type":
        return _cvxcore.IntVector2D_size(self)

    def swap(self, v: "IntVector2D") -> "void":
        return _cvxcore.IntVector2D_swap(self, v)

    def begin(self) -> "std::vector< std::vector< int > >::iterator":
        return _cvxcore.IntVector2D_begin(self)

    def end(self) -> "std::vector< std::vector< int > >::iterator":
        return _cvxcore.IntVector2D_end(self)

    def rbegin(self) -> "std::vector< std::vector< int > >::reverse_iterator":
        return _cvxcore.IntVector2D_rbegin(self)

    def rend(self) -> "std::vector< std::vector< int > >::reverse_iterator":
        return _cvxcore.IntVector2D_rend(self)

    def clear(self) -> "void":
        return _cvxcore.IntVector2D_clear(self)

    def get_allocator(self) -> "std::vector< std::vector< int > >::allocator_type":
        return _cvxcore.IntVector2D_get_allocator(self)

    def pop_back(self) -> "void":
        return _cvxcore.IntVector2D_pop_back(self)

    def erase(self, *args) -> "std::vector< std::vector< int > >::iterator":
        return _cvxcore.IntVector2D_erase(self, *args)

    def __init__(self, *args):
        _cvxcore.IntVector2D_swiginit(self, _cvxcore.new_IntVector2D(*args))

    def push_back(self, x: "IntVector") -> "void":
        return _cvxcore.IntVector2D_push_back(self, x)

    def front(self) -> "std::vector< std::vector< int > >::value_type const &":
        return _cvxcore.IntVector2D_front(self)

    def back(self) -> "std::vector< std::vector< int > >::value_type const &":
        return _cvxcore.IntVector2D_back(self)

    def assign(self, n: "std::vector< std::vector< int > >::size_type", x: "IntVector") -> "void":
        return _cvxcore.IntVector2D_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _cvxcore.IntVector2D_resize(self, *args)

    def insert(self, *args) -> "void":
        return _cvxcore.IntVector2D_insert(self, *args)

    def reserve(self, n: "std::vector< std::vector< int > >::size_type") -> "void":
        return _cvxcore.IntVector2D_reserve(self, n)

    def capacity(self) -> "std::vector< std::vector< int > >::size_type":
        return _cvxcore.IntVector2D_capacity(self)
    __swig_destroy__ = _cvxcore.delete_IntVector2D

# Register IntVector2D in _cvxcore:
_cvxcore.IntVector2D_swigregister(IntVector2D)

class DoubleVector2D(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.DoubleVector2D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _cvxcore.DoubleVector2D___nonzero__(self)

    def __bool__(self) -> "bool":
        return _cvxcore.DoubleVector2D___bool__(self)

    def __len__(self) -> "std::vector< std::vector< double > >::size_type":
        return _cvxcore.DoubleVector2D___len__(self)

    def __getslice__(self, i: "std::vector< std::vector< double > >::difference_type", j: "std::vector< std::vector< double > >::difference_type") -> "std::vector< std::vector< double,std::allocator< double > >,std::allocator< std::vector< double,std::allocator< double > > > > *":
        return _cvxcore.DoubleVector2D___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _cvxcore.DoubleVector2D___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< std::vector< double > >::difference_type", j: "std::vector< std::vector< double > >::difference_type") -> "void":
        return _cvxcore.DoubleVector2D___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _cvxcore.DoubleVector2D___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< std::vector< double > >::value_type const &":
        return _cvxcore.DoubleVector2D___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _cvxcore.DoubleVector2D___setitem__(self, *args)

    def pop(self) -> "std::vector< std::vector< double > >::value_type":
        return _cvxcore.DoubleVector2D_pop(self)

    def append(self, x: "DoubleVector") -> "void":
        return _cvxcore.DoubleVector2D_append(self, x)

    def empty(self) -> "bool":
        return _cvxcore.DoubleVector2D_empty(self)

    def size(self) -> "std::vector< std::vector< double > >::size_type":
        return _cvxcore.DoubleVector2D_size(self)

    def swap(self, v: "DoubleVector2D") -> "void":
        return _cvxcore.DoubleVector2D_swap(self, v)

    def begin(self) -> "std::vector< std::vector< double > >::iterator":
        return _cvxcore.DoubleVector2D_begin(self)

    def end(self) -> "std::vector< std::vector< double > >::iterator":
        return _cvxcore.DoubleVector2D_end(self)

    def rbegin(self) -> "std::vector< std::vector< double > >::reverse_iterator":
        return _cvxcore.DoubleVector2D_rbegin(self)

    def rend(self) -> "std::vector< std::vector< double > >::reverse_iterator":
        return _cvxcore.DoubleVector2D_rend(self)

    def clear(self) -> "void":
        return _cvxcore.DoubleVector2D_clear(self)

    def get_allocator(self) -> "std::vector< std::vector< double > >::allocator_type":
        return _cvxcore.DoubleVector2D_get_allocator(self)

    def pop_back(self) -> "void":
        return _cvxcore.DoubleVector2D_pop_back(self)

    def erase(self, *args) -> "std::vector< std::vector< double > >::iterator":
        return _cvxcore.DoubleVector2D_erase(self, *args)

    def __init__(self, *args):
        _cvxcore.DoubleVector2D_swiginit(self, _cvxcore.new_DoubleVector2D(*args))

    def push_back(self, x: "DoubleVector") -> "void":
        return _cvxcore.DoubleVector2D_push_back(self, x)

    def front(self) -> "std::vector< std::vector< double > >::value_type const &":
        return _cvxcore.DoubleVector2D_front(self)

    def back(self) -> "std::vector< std::vector< double > >::value_type const &":
        return _cvxcore.DoubleVector2D_back(self)

    def assign(self, n: "std::vector< std::vector< double > >::size_type", x: "DoubleVector") -> "void":
        return _cvxcore.DoubleVector2D_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _cvxcore.DoubleVector2D_resize(self, *args)

    def insert(self, *args) -> "void":
        return _cvxcore.DoubleVector2D_insert(self, *args)

    def reserve(self, n: "std::vector< std::vector< double > >::size_type") -> "void":
        return _cvxcore.DoubleVector2D_reserve(self, n)

    def capacity(self) -> "std::vector< std::vector< double > >::size_type":
        return _cvxcore.DoubleVector2D_capacity(self)
    __swig_destroy__ = _cvxcore.delete_DoubleVector2D

# Register DoubleVector2D in _cvxcore:
_cvxcore.DoubleVector2D_swigregister(DoubleVector2D)

class IntIntMap(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.IntIntMap_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _cvxcore.IntIntMap___nonzero__(self)

    def __bool__(self) -> "bool":
        return _cvxcore.IntIntMap___bool__(self)

    def __len__(self) -> "std::map< int,int >::size_type":
        return _cvxcore.IntIntMap___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key: "std::map< int,int >::key_type const &") -> "std::map< int,int >::mapped_type const &":
        return _cvxcore.IntIntMap___getitem__(self, key)

    def __delitem__(self, key: "std::map< int,int >::key_type const &") -> "void":
        return _cvxcore.IntIntMap___delitem__(self, key)

    def has_key(self, key: "std::map< int,int >::key_type const &") -> "bool":
        return _cvxcore.IntIntMap_has_key(self, key)

    def keys(self) -> "PyObject *":
        return _cvxcore.IntIntMap_keys(self)

    def values(self) -> "PyObject *":
        return _cvxcore.IntIntMap_values(self)

    def items(self) -> "PyObject *":
        return _cvxcore.IntIntMap_items(self)

    def __contains__(self, key: "std::map< int,int >::key_type const &") -> "bool":
        return _cvxcore.IntIntMap___contains__(self, key)

    def key_iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.IntIntMap_key_iterator(self)

    def value_iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.IntIntMap_value_iterator(self)

    def __setitem__(self, *args) -> "void":
        return _cvxcore.IntIntMap___setitem__(self, *args)

    def asdict(self) -> "PyObject *":
        return _cvxcore.IntIntMap_asdict(self)

    def __init__(self, *args):
        _cvxcore.IntIntMap_swiginit(self, _cvxcore.new_IntIntMap(*args))

    def empty(self) -> "bool":
        return _cvxcore.IntIntMap_empty(self)

    def size(self) -> "std::map< int,int >::size_type":
        return _cvxcore.IntIntMap_size(self)

    def swap(self, v: "IntIntMap") -> "void":
        return _cvxcore.IntIntMap_swap(self, v)

    def begin(self) -> "std::map< int,int >::iterator":
        return _cvxcore.IntIntMap_begin(self)

    def end(self) -> "std::map< int,int >::iterator":
        return _cvxcore.IntIntMap_end(self)

    def rbegin(self) -> "std::map< int,int >::reverse_iterator":
        return _cvxcore.IntIntMap_rbegin(self)

    def rend(self) -> "std::map< int,int >::reverse_iterator":
        return _cvxcore.IntIntMap_rend(self)

    def clear(self) -> "void":
        return _cvxcore.IntIntMap_clear(self)

    def get_allocator(self) -> "std::map< int,int >::allocator_type":
        return _cvxcore.IntIntMap_get_allocator(self)

    def count(self, x: "std::map< int,int >::key_type const &") -> "std::map< int,int >::size_type":
        return _cvxcore.IntIntMap_count(self, x)

    def erase(self, *args) -> "void":
        return _cvxcore.IntIntMap_erase(self, *args)

    def find(self, x: "std::map< int,int >::key_type const &") -> "std::map< int,int >::iterator":
        return _cvxcore.IntIntMap_find(self, x)

    def lower_bound(self, x: "std::map< int,int >::key_type const &") -> "std::map< int,int >::iterator":
        return _cvxcore.IntIntMap_lower_bound(self, x)

    def upper_bound(self, x: "std::map< int,int >::key_type const &") -> "std::map< int,int >::iterator":
        return _cvxcore.IntIntMap_upper_bound(self, x)
    __swig_destroy__ = _cvxcore.delete_IntIntMap

# Register IntIntMap in _cvxcore:
_cvxcore.IntIntMap_swigregister(IntIntMap)

class LinOpVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.LinOpVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _cvxcore.LinOpVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _cvxcore.LinOpVector___bool__(self)

    def __len__(self) -> "std::vector< LinOp * >::size_type":
        return _cvxcore.LinOpVector___len__(self)

    def __getslice__(self, i: "std::vector< LinOp * >::difference_type", j: "std::vector< LinOp * >::difference_type") -> "std::vector< LinOp *,std::allocator< LinOp * > > *":
        return _cvxcore.LinOpVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _cvxcore.LinOpVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< LinOp * >::difference_type", j: "std::vector< LinOp * >::difference_type") -> "void":
        return _cvxcore.LinOpVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _cvxcore.LinOpVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< LinOp * >::value_type":
        return _cvxcore.LinOpVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _cvxcore.LinOpVector___setitem__(self, *args)

    def pop(self) -> "std::vector< LinOp * >::value_type":
        return _cvxcore.LinOpVector_pop(self)

    def append(self, x: "LinOp") -> "void":
        return _cvxcore.LinOpVector_append(self, x)

    def empty(self) -> "bool":
        return _cvxcore.LinOpVector_empty(self)

    def size(self) -> "std::vector< LinOp * >::size_type":
        return _cvxcore.LinOpVector_size(self)

    def swap(self, v: "LinOpVector") -> "void":
        return _cvxcore.LinOpVector_swap(self, v)

    def begin(self) -> "std::vector< LinOp * >::iterator":
        return _cvxcore.LinOpVector_begin(self)

    def end(self) -> "std::vector< LinOp * >::iterator":
        return _cvxcore.LinOpVector_end(self)

    def rbegin(self) -> "std::vector< LinOp * >::reverse_iterator":
        return _cvxcore.LinOpVector_rbegin(self)

    def rend(self) -> "std::vector< LinOp * >::reverse_iterator":
        return _cvxcore.LinOpVector_rend(self)

    def clear(self) -> "void":
        return _cvxcore.LinOpVector_clear(self)

    def get_allocator(self) -> "std::vector< LinOp * >::allocator_type":
        return _cvxcore.LinOpVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _cvxcore.LinOpVector_pop_back(self)

    def erase(self, *args) -> "std::vector< LinOp * >::iterator":
        return _cvxcore.LinOpVector_erase(self, *args)

    def __init__(self, *args):
        _cvxcore.LinOpVector_swiginit(self, _cvxcore.new_LinOpVector(*args))

    def push_back(self, x: "LinOp") -> "void":
        return _cvxcore.LinOpVector_push_back(self, x)

    def front(self) -> "std::vector< LinOp * >::value_type":
        return _cvxcore.LinOpVector_front(self)

    def back(self) -> "std::vector< LinOp * >::value_type":
        return _cvxcore.LinOpVector_back(self)

    def assign(self, n: "std::vector< LinOp * >::size_type", x: "LinOp") -> "void":
        return _cvxcore.LinOpVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _cvxcore.LinOpVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _cvxcore.LinOpVector_insert(self, *args)

    def reserve(self, n: "std::vector< LinOp * >::size_type") -> "void":
        return _cvxcore.LinOpVector_reserve(self, n)

    def capacity(self) -> "std::vector< LinOp * >::size_type":
        return _cvxcore.LinOpVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_LinOpVector

# Register LinOpVector in _cvxcore:
_cvxcore.LinOpVector_swigregister(LinOpVector)

class ConstLinOpVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _cvxcore.ConstLinOpVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _cvxcore.ConstLinOpVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _cvxcore.ConstLinOpVector___bool__(self)

    def __len__(self) -> "std::vector< LinOp const * >::size_type":
        return _cvxcore.ConstLinOpVector___len__(self)

    def __getslice__(self, i: "std::vector< LinOp const * >::difference_type", j: "std::vector< LinOp const * >::difference_type") -> "std::vector< LinOp const *,std::allocator< LinOp const * > > *":
        return _cvxcore.ConstLinOpVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _cvxcore.ConstLinOpVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< LinOp const * >::difference_type", j: "std::vector< LinOp const * >::difference_type") -> "void":
        return _cvxcore.ConstLinOpVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _cvxcore.ConstLinOpVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< LinOp const * >::value_type":
        return _cvxcore.ConstLinOpVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _cvxcore.ConstLinOpVector___setitem__(self, *args)

    def pop(self) -> "std::vector< LinOp const * >::value_type":
        return _cvxcore.ConstLinOpVector_pop(self)

    def append(self, x: "LinOp") -> "void":
        return _cvxcore.ConstLinOpVector_append(self, x)

    def empty(self) -> "bool":
        return _cvxcore.ConstLinOpVector_empty(self)

    def size(self) -> "std::vector< LinOp const * >::size_type":
        return _cvxcore.ConstLinOpVector_size(self)

    def swap(self, v: "ConstLinOpVector") -> "void":
        return _cvxcore.ConstLinOpVector_swap(self, v)

    def begin(self) -> "std::vector< LinOp const * >::iterator":
        return _cvxcore.ConstLinOpVector_begin(self)

    def end(self) -> "std::vector< LinOp const * >::iterator":
        return _cvxcore.ConstLinOpVector_end(self)

    def rbegin(self) -> "std::vector< LinOp const * >::reverse_iterator":
        return _cvxcore.ConstLinOpVector_rbegin(self)

    def rend(self) -> "std::vector< LinOp const * >::reverse_iterator":
        return _cvxcore.ConstLinOpVector_rend(self)

    def clear(self) -> "void":
        return _cvxcore.ConstLinOpVector_clear(self)

    def get_allocator(self) -> "std::vector< LinOp const * >::allocator_type":
        return _cvxcore.ConstLinOpVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _cvxcore.ConstLinOpVector_pop_back(self)

    def erase(self, *args) -> "std::vector< LinOp const * >::iterator":
        return _cvxcore.ConstLinOpVector_erase(self, *args)

    def __init__(self, *args):
        _cvxcore.ConstLinOpVector_swiginit(self, _cvxcore.new_ConstLinOpVector(*args))

    def push_back(self, x: "LinOp") -> "void":
        return _cvxcore.ConstLinOpVector_push_back(self, x)

    def front(self) -> "std::vector< LinOp const * >::value_type":
        return _cvxcore.ConstLinOpVector_front(self)

    def back(self) -> "std::vector< LinOp const * >::value_type":
        return _cvxcore.ConstLinOpVector_back(self)

    def assign(self, n: "std::vector< LinOp const * >::size_type", x: "LinOp") -> "void":
        return _cvxcore.ConstLinOpVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _cvxcore.ConstLinOpVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _cvxcore.ConstLinOpVector_insert(self, *args)

    def reserve(self, n: "std::vector< LinOp const * >::size_type") -> "void":
        return _cvxcore.ConstLinOpVector_reserve(self, n)

    def capacity(self) -> "std::vector< LinOp const * >::size_type":
        return _cvxcore.ConstLinOpVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_ConstLinOpVector

# Register ConstLinOpVector in _cvxcore:
_cvxcore.ConstLinOpVector_swigregister(ConstLinOpVector)


def build_matrix(*args) -> "ProblemData":
    return _cvxcore.build_matrix(*args)


