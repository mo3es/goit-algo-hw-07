class Comment:

    def __init__(self, comment, author):
        self.left = None
        self.right = None
        self.val = comment
        self.author = author + ':'
        self.is_deleted = False

    def __str__(self, level=0):
        ret = "\t" * level + str(self.author) + ' ' + str(self.val) + "\n"
        
        if self.right:
            ret += self.right.__str__(level + 1)
        if self.left:
            ret += self.left.__str__(level)
        return ret

    def display(self):
        print(self)

    def add_reply(self, comment):
        if self.right is None:
            self.right = comment
        else:
            current = self.right
            while current.left:
                current = current.left
            current.left = comment


    def remove_reply(self):
        self.val = 'було видалено.'
        self.author = 'Цей коментар'
        self.is_deleted = True



root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
