user = input("File name: ").strip().lower()
if "." in user:
    suffix = user.split(".")[-1]
    match suffix:
        case "jpg" |"jpeg":
            print("image/jpeg")
        case "gif" |"png":
            print(f"image/{suffix}")
        case  "pdf"|"zip":
            print(f"application/{suffix}")
        case "txt":
            print(f"text/{user.split(".")[0]}")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
