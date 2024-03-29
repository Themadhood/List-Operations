

try:
    from .stack_array import Stack as stack_array,SimpleArray
    from .stack_linked import Stack as stack_linked
except:
    from stack_array import Stack as stack_array,SimpleArray
    from stack_linked import Stack as stack_linked


