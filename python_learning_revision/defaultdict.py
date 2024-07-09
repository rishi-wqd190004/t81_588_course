
site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
from collections import defaultdict

validated_locations = defaultdict(lambda: 'TODO: Add to website')

validated_locations.update(site_locations)

for prod in updated_products:
  if prod not in site_locations.keys():
    site_locations[prod] = validated_locations[prod]

print(site_locations)


