# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.__current_channel = self.channels[0]

    def first_channel(self):
        self.__current_channel = self.channels[0]
        print('Turned to the first channel')

    def last_channel(self):
        self.__current_channel = self.channels[-1]
        print('Turned to the last channel')

    def turn_channel(self, n=1):
        try:
            self.__current_channel = self.channels[n-1]
            print(f'Turned to the {n} channel')
        except IndexError:
            print(f'There are only {len(self.channels)} channels available!')

    def next_channel(self):
        if self.__current_channel == self.channels[-1]:
            self.__current_channel = self.channels[0]
        else:
            self.__current_channel = self.channels[self.channels.index(self.__current_channel) + 1]
        print('Turned to the next channel')

    def previous_channel(self):
        if self.__current_channel == self.channels[0]:
            self.__current_channel = self.channels[-1]
        else:
            self.__current_channel = self.channels[self.channels.index(self.__current_channel) - 1]
        print('Turned to the previous channel')

    def current_channel(self):
        return self.__current_channel

    def is_exist(self, name='0'):
        try:
            name = int(name.strip())
            if name > 0 and name-1 < len(self.channels):
                return 'Yes'
            else:
                return 'No'
        except ValueError:
            if name in self.channels:
                return 'Yes'
            else:
                return 'No'



if __name__ == '__main__':
    my_TVController = TVController(CHANNELS)

    while 1:
        what_to_do = input(f'''You are watching {my_TVController.current_channel()}.\nTo check other channels please enter:
        f - to turn to the first channel
        l - for the last channel
        t - to turn to the specified channel
        n - for the next channel
        p - for the previous channel
        c - to check your current channel
        x - to check if the specified channel exists
        q - to exit\n''').strip().lower()


        if what_to_do == 'f':
            my_TVController.first_channel()

        elif what_to_do == 'l':
            my_TVController.last_channel()

        elif what_to_do == 't':
            channel_to_turn = input('Which channel do you want to turn to? ').strip()
            try:
                channel_to_turn = int(channel_to_turn)
                my_TVController.turn_channel(n=channel_to_turn)
            except ValueError:
                print(f'Do you really think that {channel_to_turn} is a number? o_O')

        elif what_to_do == 'n':
            my_TVController.next_channel()

        elif what_to_do == 'p':
            my_TVController.previous_channel()

        elif what_to_do == 'c':
            print(f'You current channel is {my_TVController.current_channel()}')

        elif what_to_do == 'x':
            channel_to_check = input('Please enter number or name of the channel which you want to check: ')
            print(f'Does {channel_to_check} exist? - ' + my_TVController.is_exist(name=channel_to_check))

        elif what_to_do == 'q':
            break

        else:
            print('Invalid command. Try again.\n')

