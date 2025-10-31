import customtkinter as ctk


class MotorSettingsPage:
    """Motor Settings page with navigation buttons"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_motor_settings_page()
    
    def create_motor_settings_page(self):
        """Create the Motor Settings page layout"""
        # Main container
        main_container = ctk.CTkFrame(self.parent_frame, fg_color="#F5F5F5")
        main_container.pack(fill="both", expand=True, padx=60, pady=40)
        
        # Create buttons
        buttons = [
            "System Control\nParameter",
            "Drive  Control\nParameter",
            "System Status",
            "Manufacturer\nSettings"
        ]
        
        for button_text in buttons:
            self.create_gradient_button(main_container, button_text)
    
    def create_gradient_button(self, parent, text):
        """Create a gradient button (yellow to orange)"""
        # Button with gradient effect
        button = ctk.CTkButton(
            parent,
            text=text,
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#2D2D2D",
            fg_color="#FFB84D",  # Orange color
            hover_color="#FFA73D",
            corner_radius=30,
            width=220,
            height=65
        )
        button.pack(pady=15)
