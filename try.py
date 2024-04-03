from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class ClickerApp(App):
    def build(self):
        self.score = 0
        self.time_remaining = 60  # Time limit for the game (in seconds)

        # Create a label to display the score
        self.score_label = Label(text=f'Score: {self.score}', size_hint=(None, None), size=(150, 50))

        # Create a button for the player to click
        self.click_button = Button(text='Click Me!', size_hint=(None, None), size=(200, 100))
        self.click_button.bind(on_press=self.on_click)

        # Create a label to display the time remaining
        self.timer_label = Label(text=f'Time Remaining: {self.time_remaining}', size_hint=(None, None), size=(200, 50))

        # Schedule the countdown timer
        Clock.schedule_interval(self.update_timer, 1)

        # Create a box layout and add UI components to it
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.score_label)
        layout.add_widget(self.click_button)
        layout.add_widget(self.timer_label)

        return layout

    def update_timer(self, dt):
        # Update the time remaining and update the timer label
        self.time_remaining -= 1
        self.timer_label.text = f'Time Remaining: {self.time_remaining}'

        # End the game if time runs out
        if self.time_remaining == 0:
            self.click_button.disabled = True  # Disable the button
            self.click_button.text = 'Time\'s Up!'
            return False  # Stop the countdown

    def on_click(self, instance):
        # Increment the score when the button is clicked
        self.score += 1
        self.score_label.text = f'Score: {self.score}'

if __name__ == '__main__':
    ClickerApp().run()
