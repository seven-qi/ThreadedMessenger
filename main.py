from threadedmessenger.message import Message 
from threadedmessenger.threadlist import ThreadList

def main():
    """
    Test ThreadList class str method.
    """
    # Create a new thread list that shows only the top 3 threads.
    # State: []
    threadlist = ThreadList(3)
    print "Create a new thread list that shows only the top 3 threads."
    print "State: "
    threadlist.display()
    print ""

    # Add (M7, T13). State: [7(13)]
    message_13 = Message(13, "Head of Message 13", "Content of Message 13")
    threadlist.add(message_13, 7)
    print "State: "
    threadlist.display()
    print ""

    # Add (M5, T99). State: [99(5), 7(13)]
    message_5 = Message(5, "Head of Message 5", "Content of Message 5")
    threadlist.add(message_5, 99)
    print "Add (M5, T99)"
    print "State: "
    threadlist.display()
    print ""

    # Add (M4, T11). State: [11(4), 99(5), 7(13)]
    message_4 = Message(4, "Head of Message 4", "Content of Message 4")
    threadlist.add(message_4, 11)
    print "Add (M4, T11)"
    print "State: "
    threadlist.display()
    print ""

    # Add (M44, T99). State: [99(44, 5), 11(4), 7(13)]
    message_44 = Message(44, "Head of Message 44", "Content of Message 44")
    threadlist.add(message_44, 99)
    print "Add (M44, T99)"
    print "State: "
    threadlist.display()
    print ""

    # Add (M1, T11). State: [1(1), 99(44, 55), 11(4), 7(13)] => [[1(1), 99(44, 55), 11(4)]
    message_1 = Message(1, "Head of Message 1", "Content of Message 1")
    threadlist.add(message_1, 1)
    print "Add (M1, T11)"
    print "State: "
    threadlist.display()
    print ""

    # Add (M2, T7). State: [7(2, 13), 1(1), 99(44, 55), 11(4)] => [7(2, 13), 1(1), 99(44, 55)]
    message_2 = Message(2, "Head of Message 2", "Content of Message 2")
    threadlist.add(message_2, 7)
    print "Add (M2, T7)"
    print "State: "
    threadlist.display()
    print ""

if __name__ == '__main__':
    main()