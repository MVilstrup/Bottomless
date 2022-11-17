from bottomless.api.parser.language.base import element

"""
Builtin modules
"""
Auth = element(token="Auth", tag=r'auth')
Error = element(token="Error", tag=r'error')
Retry = element(token="Retry", tag=r'retry')
Now = element(token="Now", tag=r'now')

""" 
    Event Initiator 
"""
Derived = element(token="Derived", tag=r'deruived')
On = element(token="On", tag=r'on')

""" 
    Event Modifiers 
"""
Will = element(token="will", tag=r'will')
Did = element(token="will", tag=r'will')
Failure = element(token="Failure", tag=r'failure')

"""
    Dynamic Pointers
"""
This = element(token="This", tag=r'this')
Next = element(token="Next", tag=r'next')

"""
    Event Listeners and Triggers
"""
Creation = element(token="Creation", tag=r'creation')
Update = element(token="Update", tag=r'update')
Delete = element(token="Delete", tag=r'delete')
Startup = element(token="Delete", tag=r'delete')
Shutdown = element(token="Delete", tag=r'delete')
Retrieval = element(token="Retrieval", tag=r'retrieval')
ErrorEvent = element(token="ErrorType", tag=r'error\.[a-ZA-z]+')
Success = element(token="Success", tag=r'success')
LockDown = element(token="LockDown", tag=r'lockdown')
Publish = element(token="Publish", tag=r'publish')
Subscribe = element(token="Subscribe", tag=r'subscribe')

"""
Action Patterns
"""
Do = element(token="Do", tag=r'do')
With = element(token="With", tag=r'with')
Check = element(token="Check", tag=r'check')
Set = element(token="Set", tag=r'set')
To = element(token="To", tag=r'to')
If = element(token="If", tag=r'if')
Then = element(token="Then", tag=r'then')
Else = element(token="Else", tag=r'else')

"""
Functions
"""
Ref = element(token="Ref", tag=r'ref')
Children = element(token="Children", tag=r'children')
Part = element(token="Part", tag=r'part')
Include = element(token="Include", tag=r'include')
Time = element(token="Time", tag=r'time')

"""
Types
"""
Import = element(token="Import", tag=r'import')

Function = element(token="Function", tag=r'func')
App = element(token="App", tag=r'func')
Type = element(token="Type", tag=r'type')
Module = element(token="Module", tag=r'module')
Constant = element(token="Constant", tag=r'const')

Query = element(token="Query", tag=r'query')
Mutation = element(token="Mutation", tag=r'mutation')
Route = element(token="Route", tag=r'route')
Socket = element(token="Socket", tag=r'socket')
Pulse = element(token="Pulse", tag=r'scheduler')

"""
Scalar Value Types
"""
Integer = element(token="Integer", tag=r'int')
Float = element(token="Float", tag=r'float')
String = element(token="String", tag=r'str')
Boolean = element(token="Boolean", tag=r'bool')
DateTime = element(token="DateTime", tag=r'datetime')

Any = element(token="Any", tag=r'Any')
Scalar = element(token="Scalar", tag=r'Scalar')
NoneType = element(token="None", tag=r'None')

"""
    Constraints
"""
Subscriptable = element(token="Subscriptable", tag=r'subscriptable')
Unique = element(token="Unique", tag=r'unique')
NotNull = element(token="NotNull", tag=r'!')
