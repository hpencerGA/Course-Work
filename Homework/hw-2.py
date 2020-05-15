
worker_type = 'part_time'
hours_worked = 25
wage = 0
tax_rate = .25
tax_dollar = 0

if worker_type == "full_time":
    if hours_worked < 40:
        wage = 50 * hours_worked
    else:
        wage = (50 * 40) + ((hours_worked-40) * 60)
elif worker_type == 'part_time':
    if hours_worked < 20:
        wage = 65 * hours_worked
    else:
        wage = (65 * 20) + ((hours_worked-20) * 70)
elif worker_type == 'contract':
    wage = 120 * hours_worked
    tax_dollar = (wage * tax_rate)

print (f' {worker_type} employee weekly wage {wage - tax_dollar}')