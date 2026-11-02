def main() -> None:
    document_stack = []
    redo_stack = []

    while (command := input("type/undo/redo/quit: ")) != "quit":
        if command == "type":
            document_stack.append(input(": "))
            redo_stack = []
            print("Document: ", *document_stack, sep="")
        elif command == "undo":
            if document_stack:
                redo_stack.append(document_stack.pop())
                print("Document: ", *document_stack, sep="")
            else:
                print("Nothing to undo")
        elif command == "redo":
            if redo_stack:
                document_stack.append(redo_stack.pop())
                print("Document: ", *document_stack, sep="")
            else:
                print("Nothing to redo")


if __name__ == "__main__":
    main()
