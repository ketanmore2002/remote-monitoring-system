from django import template

register = template.Library()

@register.filter
def cumulative_sum(numbers):
    total = 0
    cumulative_sums = []
    
    for num in numbers:
        total += num
        cumulative_sums.append(total)
    
    return cumulative_sums
