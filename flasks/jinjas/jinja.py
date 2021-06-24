''' Jinja2 is a tamplate engine for dynamically rendering.
A template contains HTML text with components:
          {{ <expression> }}
          {% <controls> %} 
          {# <comment> #}.
<expression> is evaluated and result is insert in the placeholders.
<controls> is processed at the server side.
Templates may be just HTML file.
'''
from jinja2 import Template

# Create a template.
t = Template('{{ exp }}')

# Render templates.
print( t.render(exp='Hello John') )     # Hello John
print( t.render(exp=1+2) )              # 3
print( t.render(exp=len('hello')) )     # 5

a = ['john', 'jack', 'joe']
print( t.render(exp=a[0]) )             # john

d = {'john': 'rambo', 'jack': 'ripper' }
print( t.render(exp=d['john']) )        # rambo

t = Template('{{ my_list[1] }}')
print( t.render(my_list=a) )            # jack

t = Template('{{ my_dict["john"] }}')
print( t.render(my_dict=d) )            # rambo

t = Template('{{ my_dict.jack }}')
print( t.render(my_dict=d) )            # ripper

# <expression> may contain function calls.
t = Template('{{ fnc(n) }}')
print( t.render(fnc=lambda x: x*x, n=2) ) # 4

# <expression> may contain method calls.
class John:
    def email(self):
        return 'john@rambo.com'
    def __repr__(self):
        return 'John Rambo'
t = Template('Name: {{ ins }} email: {{ ins.email() }}')   
print( t.render(ins=John()))
            # Name: John Rambo email: john@rambo.com

# Parameters:
t = Template('{{ a }} + {{ b }} = {{ a + b }}')
print( t.render(a=1, b= 2) )            # 1 + 2 = 3

# Variables:
t = Template('''
{% set x = 0 %}
x = {{ x }}
{% set x = x+1 %}
x = {{ x }} ''')
print( t.render())      # x = 0
                        # x = 1

#------------------------------------------------------------

# For Loop:
# Iterate a list.
t = Template('''
{% for name in my_list %}
Hello {{ name }}
{%- endfor %} ''')  # - indicates no empty new lines at each iteration.
print( t.render(my_list=a) )       # Hello john
                                   # Hello jack
                                   # Hello joe

# Iterate a dict.
t = Template('''
{% for k, v in my_dict.items() %}
{{ k }}: {{ v }}.
{%- endfor %} ''')
print( t.render(my_dict=d) )       # john: rambo
                                   # jack: ripper

# Loop index:
t = Template('''
{% for name in my_list %}
{{ loop.index }} {{ name }} 
{%- endfor %} ''')           ## Try: loop.index0, loop.revindex, loop.revindex0
print( t.render(my_list=a) )    # 1 john
                                # 2 jack
                                # 3 joe
                                
# Mark each round with cycle().
t = Template('''
{% for name in my_list %}
{{ loop.cycle('red', 'blue') }}
Hello {{ name }}
{%- endfor %} ''')
print( t.render(my_list=a) )    # Hello john
                                # red
                                # Hello jack
                                # blue
                                # Hello joe
                                # red
#-----------------------------------------------------------
# Condition:
t = Template('''
{% if name == 'John' %}
Hi John.
{% else %}
Hello {{ name }}.
{% endif %} ''')
print( t.render(name='John') )      # Hi John.

# loop.first and loop.last
t = Template('''
{% for name in my_list %}
{% if loop.first %}First round {% endif %}
{% if loop.last %}Last round {% endif %}
Hello {{ name }}.
{%- endfor %} ''')
print( t.render(my_list=a) )    # First round 
                                # Hello john.
                                # Hello jack.
                                # Last round 
                                # Hello joe.
# for-if:
t = Template('''
{% for i in [1, 2, 3, 4] if i > 2 %}
{{ loop.index }}: {{ i }}
{%- endfor %} ''')
print( t.render() )         # 1: 3
                            # 2: 4

#-------------------------------------------------------------------

# Filters:
# default
t = Template( "Hello {{ name | default('Whoever you are.') }}")
print(t.render(name='john'))        # Hello john
print(t.render())                   # Hello Whoever you are.

# capitalize, lower, upper, title
t = Template( '{{ name | title }}' )                        
print(t.render(name='john'))        # John

# length
t = Template( '{{ name | length }}' )
print(t.render(name='john'))        # 4

# int, float
t = Template( '{{ x | int }}  {{ y | float }}')
print(t.render(x = 1.7, y = 1))     # 1  1.0

# round
t = Template( '{{ 3.1415 | round(2) }}')
print(t.render())                   # 3.14
t = Template( '{{ 1.7 | round(0, "floor") }}')
print(t.render())                   # 1.0
t = Template( '{{ 1.2 | round(0, "ceil") }}')
print(t.render())                   # 2.0

# truncate
s = 'Hello how do you do?'
t = Template( '{{ mgs | truncate(10) }}' )
print(t.render(mgs=s))      # Hello...
t = Template( '{{ mgs | truncate(10, True) }}' )
print(t.render(mgs=s))      # Hello h...
              
# join
t = Template( "{{ names | join(',') }}" )                        
print(t.render(names=a))            # john,jack,joe

# tojson
t = Template( '{{ names | tojson }}' )                        
print(t.render(names=d))            # {"jack": "ripper", "john": "rambo"}
  


