from contextlib import contextmanager

# @contextmanager
# def readfile(file_name):
#     f = None
#     try:
#         f = open(file_name , 'r')
#         yield f
#     except FileNotFoundError:
#         print("file not found.")
#     else:
#         pass
        
#     finally:
#         if f is not None:
#             f.close()
#         print("Processing finished.")

# with readfile('usernames.txt') as f:
#     for username in f:
#         try:
#             if username == '\n':
#                 raise ValueError
#             else:
#                 print(username.upper())
#         except ValueError:
#             print("Empty username found.\n")


@contextmanager
def readUsernames(file_name):
    f = open(file_name)
    try:
        yield f
    finally:
        f.close()
try:
    with readUsernames("usernames.txt") as f:
        for username in f:
            if username.strip() == "":
                raise ValueError
                continue
            print(username.upper())
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Empty username found.\n")
finally:
    print("Processing finished.")
