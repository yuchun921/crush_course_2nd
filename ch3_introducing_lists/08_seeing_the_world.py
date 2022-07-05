"""Seeing the World:
Think of at least five places in the world you’d like to visit.

"""

tour_locations = ["France", "Tokyo", "Bangkok", "Paris", "Okinawa"]
print(f"Origin list: {tour_locations}")
print("---------------------------------")

# Print your list in its original order.
# Don’t worry about printing the list neatly, just print it as a raw Python list.

print('""" sorted() """')
# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(tour_locations))
# Show that your list is still in its original order by printing it.
print(tour_locations)
print("---------------------------------")

print('""" sorted(reverse=True) """')
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(tour_locations, reverse=True))
# Show that your list is still in its original order by printing it again.
print(tour_locations)
print("---------------------------------")

print('""" reverse() """')
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
tour_locations.reverse()
print(tour_locations)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
tour_locations.reverse()
print(tour_locations)
print("---------------------------------")

print('""" sort() """')
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
tour_locations.sort()
print(tour_locations)

print('""" sort(reverse=True) """')
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
tour_locations.sort(reverse=True)
print(tour_locations)
