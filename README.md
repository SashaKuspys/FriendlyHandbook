# Personal assistant - Friendly Handbook

## Description

Personal Assistant is a useful command-line interface program that includes a contact book, notes, a calculator, and can analyze folders.
Friendly Handbook can:

- save contacts with phone number, name, email, date of birth to your Address Book;
- modify and delete contacts;
- find contacts by name;
- create notes and work with them (search, edit, delete, sort);
- add notes with tags;
- sort files in the specified folder by categories (images, documents, videos, other).

## Installation

To install the program, you need to go to the folder where the installation package is located and enter **pip install** or **pip install -e** in the command line.
To check availability: command **pip install -i https://test.pypi.org/simple/ FriendlyHandbook-kobSK**

## Launching a personal assistant

In the command line, you need to enter the "assistant_bot"

## Instructions for the user

Open Personal Assistant and select a category:

- AddressBook
- NoteBook
- SortFolder
- Calculator

  ### AddressBook

  Commands for the Address Book:
  | Commands | Arguments | Result |
  |---------|:---------:|-----------|
  | help | - | Show a list of all commands |
  | hello | - | Start working with an assistant |
  | add contact | name | Add a new contact to the Address Book |
  | add phone | name, phone | Add a phone number to an existing contact |
  | add email | name, email | Add email to an existing contact |
  | add birthday | name, birthday | Add or change a birthday to an existing contact |
  | change phone | name, new phone | Change the phone number of the specified contact |
  | change email | name, new email | Change the e-mail address of the specified contact |
  | change birthday | name, old birthday, new birthday | Change the birthday of the specified contact |
  | delete contact | name | Delete a contact by the specified name from the Address Book |
  | delete phone | name, phone | Delete a contact's phone number from the Address Book |
  | delete email | name, email | Delete a contact's email from the Address Book |
  | delete birthday | name, birthday | Remove a contact's birthday from the Address Book |
  | get birthday | days | Show whose birthday it is after the entered number of days |
  | show all | - | Show all contacts from the Address Book |
  | find name | name | Find a contact |
  | exit, close, goodbye | - | Finish work and return to the main menu |

  ### NoteBook

  Commands for the NoteBook:
  | Commands | Result |
  |---------|-----------|
  | help | Show a list of all commands |
  | add note | Create a new note and save it to the "Notes" folder |
  | delete note | Delete note |
  | find by tag | Search by tags |
  | find note | Find a note by name |
  | show all notes | Display all notes |
  | add tag | Add a tag to a note |
  | change tag | Change the tag of an existing note |
  | change text | Change the text of an existing note |
  | change note | Edit note |
  | close | Finish working with Notes and return to the main menu |

  ### SortFolder

  The folder sorter allows you to sort files by the following categories:

- image: [".jpeg", ".png", ".jpg", ".svg"],
- documents: [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx",],
- audio: [".mp3", ".ogg", ".wav", ".amr"],
- video: [".avi", ".mp4", ".mov", ".mkv"],
- Archives: [".zip", ".gz", ".tar", ".rar",]
- Other: 
  During sorting, the script unpacks all archives, and then places them together with other files in new folders - images, documents, audio, video, archives and others.

Enter the path to the folder to run the script, for example: C:\Users\user\Desktop\trash

### Calculator

A simple calculator can perform basic mathematical operations.


