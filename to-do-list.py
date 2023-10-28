class TodoItem:
  def __init__(self, title, description, due_date, is_done=False):
    self.title = title
    self.description = description
    self.due_date = due_date
    self.is_done = is_done

class TodoList:
  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    self.items.remove(item)

  def get_items(self):
    return self.items

  def mark_item_as_done(self, item):
    item.is_done = True

  def print_items(self):
    for item in self.items:
      print(f"{item.title} - {item.description} ({item.due_date}) - {'Done' if item.is_done else 'Not done'}")

def main():
  todo_list = todo_list

  while True:
    command = input("What would you like to do? (add, remove, mark_as_done, print, quit): ")

    if command == "add":
      title = input("Enter the title of the to-do item: ")
      description = input("Enter the description of the to-do item: ")
      due_date = input("Enter the due date of the to-do item: ")

      item = TodoItem(title, description, due_date)
      todo_list.add_item(item)

    elif command == "remove":
      title = input("Enter the title of the to-do item to remove: ")

      for item in todo_list.get_items():
        if item.title == title:
          todo_list.remove_item(item)
          break

    elif command == "mark_as_done":
      title = input("Enter the title of the to-do item to mark as done: ")

      for item in todo_list.get_items():
        if item.title == title:
          todo_list.mark_item_as_done(item)
          break

    elif command == "print":
      todo_list.print_items()

    elif command == "quit":
      break

if __name__ == "__main__":
  main()