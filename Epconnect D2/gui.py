import customtkinter as ctk
from tkinter import messagebox
import serial.tools.list_ports
from products_page import ProductsPage
from firmware_page import FirmwarePage
from operation_settings_page import OperationSettingsPage
from motor_settings_page import MotorSettingsPage

# Set appearance mode and color theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class ePropelledDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("ePropelled Dashboard - Manufacturer")
        self.geometry("1400x800")
        self.configure(fg_color="#F5F5F5")

        # Create main container
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar
        self.create_sidebar()

        # Create main content area
        self.create_main_content()

        # Variables for device connection
        self.scanning = False
        self.baud_rates = ["9600", "19200", "38400", "57600", "115200"]
        
        # Sidebar state - start collapsed (icons only)
        self.sidebar_expanded = False
        self.current_page = "Welcome Wizard"

    def create_sidebar(self):
        """Create the left sidebar with navigation menu"""
        self.sidebar = ctk.CTkFrame(self, width=70, corner_radius=0, fg_color="white")
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.sidebar.grid_rowconfigure(20, weight=1)
        self.sidebar.grid_propagate(False)

        # Logo section with hamburger menu
        logo_frame = ctk.CTkFrame(self.sidebar, fg_color="white", height=60)
        logo_frame.grid(row=0, column=0, padx=5, pady=15, sticky="ew")
        logo_frame.grid_propagate(False)

        # Hamburger icon button to toggle sidebar
        self.hamburger_btn = ctk.CTkButton(
            logo_frame,
            text="☰",
            width=40,
            height=40,
            fg_color="#4CAF50",
            hover_color="#45a049",
            font=ctk.CTkFont(size=20),
            corner_radius=8,
            command=self.toggle_sidebar
        )
        self.hamburger_btn.pack(pady=5)

        # Navigation menu items with icons
        menu_items = [
            ("😊", "Welcome Wizard", True),
            ("📦", "Products", False),
            ("⚙️", "Firmware", False),
            ("🔧", "Operation Settings", False),
            ("⚡", "Motor Settings", False),
            ("🎯", "System Control Parameters", False),
            ("👤", "Drive Control Panel", False),
            ("🛒", "System Status", False),
            ("📋", "Diagnostics", False),
            ("📊", "Data Analysis", False),
            ("💰", "Live Dashboard", False),
            ("📝", "System Logs", False),
        ]

        self.menu_buttons = []
        for idx, (icon, item, is_active) in enumerate(menu_items):
            btn = self.create_icon_menu_button(icon, item, is_active, idx + 2)
            self.menu_buttons.append(btn)

        # Bottom menu items with icons
        bottom_items = [
            ("❓", "Help", 22),
            ("🚪", "Log out", 23),
            ("⚙️", "Settings", 24),
        ]

        for icon, item, row in bottom_items:
            self.create_icon_menu_button(icon, item, False, row, is_bottom=True)

    def create_icon_menu_button(self, icon, text, is_active, row, is_bottom=False):
        """Create a menu button with icon that shows/hides text"""
        fg_color = "#C8E6C9" if is_active else "transparent"
        hover_color = "#E8F5E9" if not is_active else "#B2DFB2"
        text_color = "#2D2D2D" if is_active else "#666666"

        btn = ctk.CTkButton(
            self.sidebar,
            text=icon,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            corner_radius=8,
            height=40,
            width=50,
            font=ctk.CTkFont(size=18),
            border_width=0,
            command=lambda: self.menu_icon_clicked(icon, text, btn)
        )
        
        pady = (0, 5) if not is_bottom else (5, 5)
        btn.grid(row=row, column=0, padx=10, pady=pady)
        
        # Store button data
        btn.menu_text = text
        btn.icon = icon
        btn.is_active = is_active
        
        return btn
    
    def toggle_sidebar(self):
        """Toggle sidebar between collapsed (icons only) and expanded (icons + text)"""
        self.sidebar_expanded = not self.sidebar_expanded
        
        if self.sidebar_expanded:
            # Expand sidebar to show text
            self.sidebar.configure(width=250)
            for btn in self.menu_buttons:
                btn.configure(
                    text=f"{btn.icon}  {btn.menu_text}",
                    width=220,
                    anchor="w"
                )
        else:
            # Collapse sidebar to show only icons
            self.sidebar.configure(width=70)
            for btn in self.menu_buttons:
                btn.configure(
                    text=btn.icon,
                    width=50,
                    anchor="center"
                )

    def menu_icon_clicked(self, icon, menu_name, btn):
        """Handle menu icon clicks - toggle sidebar and navigate"""
        # Update active state
        self.current_page = menu_name
        for button in self.menu_buttons:
            if button.menu_text == menu_name:
                button.configure(fg_color="#C8E6C9")
                button.is_active = True
            else:
                button.configure(fg_color="transparent")
                button.is_active = False
        
        # Toggle sidebar expansion
        if not self.sidebar_expanded:
            self.toggle_sidebar()
        
        # Load the selected page
        self.load_page(menu_name)
    
    def load_page(self, page_name):
        """Load the selected page content"""
        # Clear existing content in scroll_frame
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
        
        # Load the appropriate page
        if page_name == "Welcome Wizard":
            self.load_welcome_wizard_page()
        elif page_name == "Products":
            self.load_products_page()
        elif page_name == "Firmware":
            self.load_firmware_page()
        elif page_name == "Operation Settings":
            self.load_operation_settings_page()
        elif page_name == "Motor Settings":
            self.load_motor_settings_page()
        else:
            # Placeholder for other pages
            placeholder = ctk.CTkLabel(
                self.scroll_frame,
                text=f"{page_name} - Coming Soon",
                font=ctk.CTkFont(size=24, weight="bold"),
                text_color="#666666"
            )
            placeholder.pack(pady=50)
    
    def load_welcome_wizard_page(self):
        """Load Welcome Wizard page content"""
        # Info Bar section
        self.create_info_bar_section()
        
        # Device Status section
        self.create_device_status_section()
        
        # System Status section with tabs
        self.create_system_status_section()
    
    def load_products_page(self):
        """Load Products page content"""
        ProductsPage(self.scroll_frame)
    
    def load_firmware_page(self):
        """Load Firmware page content"""
        FirmwarePage(self.scroll_frame)
    
    def load_operation_settings_page(self):
        """Load Operation Settings page content"""
        OperationSettingsPage(self.scroll_frame)
    
    def load_motor_settings_page(self):
        """Load Motor Settings page content"""
        MotorSettingsPage(self.scroll_frame)

    def create_main_content(self):
        """Create the main content area"""
        # Main content frame
        self.main_content = ctk.CTkFrame(self, corner_radius=0, fg_color="#F5F5F5")
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main_content.grid_columnconfigure(0, weight=1)

        # Header with logo
        self.create_header()

        # Content area with scrollable frame
        self.scroll_frame = ctk.CTkScrollableFrame(
            self.main_content,
            fg_color="#F5F5F5",
            corner_radius=0
        )
        self.scroll_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=20)
        self.main_content.grid_rowconfigure(1, weight=1)

        # Load initial page (Welcome Wizard)
        self.load_welcome_wizard_page()

    def create_header(self):
        """Create the header with ePropelled logo"""
        header_frame = ctk.CTkFrame(self.main_content, fg_color="white", height=100, corner_radius=0)
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header_frame.grid_propagate(False)

        # ePROPELLED logo
        logo_title = ctk.CTkLabel(
            header_frame,
            text="ePROPELLED™",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#D32F2F"
        )
        logo_title.pack(pady=10)

        subtitle = ctk.CTkLabel(
            header_frame,
            text="UNSCREWED, UNLIMITED",
            font=ctk.CTkFont(size=12),
            text_color="#999999"
        )
        subtitle.pack()

    def create_info_bar_section(self):
        """Create the Info Bar section"""
        # Info Bar title
        info_title = ctk.CTkLabel(
            self.scroll_frame,
            text="Info Bar",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2D2D2D",
            anchor="w"
        )
        info_title.pack(fill="x", pady=(0, 10))

        # Info Bar description frame
        info_desc_frame = ctk.CTkFrame(
            self.scroll_frame,
            fg_color="white",
            corner_radius=10
        )
        info_desc_frame.pack(fill="x", pady=(0, 30))

        info_text = (
            "The InfoBar control is for displaying app-wide status messages to users that\n"
            "are highly visible yet non-intrusive. There are built-in Severity levels to\n"
            "easily indicate the type of message shown as well as the option to include\n"
            "your own call to action or hyperlink button. Since the InfoBar is inline with\n"
            "other UI content the option is there for the control to always be visible or\n"
            "dismissed by the user."
        )

        info_label = ctk.CTkLabel(
            info_desc_frame,
            text=info_text,
            font=ctk.CTkFont(size=13),
            text_color="#555555",
            anchor="w",
            justify="left"
        )
        info_label.pack(padx=30, pady=30, fill="x")

    def create_device_status_section(self):
        """Create the Device Status section"""
        # Device Status container
        device_frame = ctk.CTkFrame(
            self.scroll_frame,
            fg_color="white",
            corner_radius=10
        )
        device_frame.pack(fill="both", expand=True, pady=(0, 20))

        # Title
        device_title = ctk.CTkLabel(
            device_frame,
            text="Device Status",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#2D2D2D"
        )
        device_title.pack(pady=(30, 30))

        # Scanning For Device section
        scan_label = ctk.CTkLabel(
            device_frame,
            text="Scanning For Device",
            font=ctk.CTkFont(size=13),
            text_color="#666666"
        )
        scan_label.pack(pady=(0, 10))

        self.device_entry = ctk.CTkEntry(
            device_frame,
            width=400,
            height=40,
            corner_radius=8,
            fg_color="#F8F8F8",
            border_width=1,
            border_color="#E0E0E0"
        )
        self.device_entry.pack(pady=(0, 15))

        self.scan_button = ctk.CTkButton(
            device_frame,
            text="scan",
            width=120,
            height=35,
            corner_radius=6,
            fg_color="#2196F3",
            hover_color="#1976D2",
            font=ctk.CTkFont(size=13),
            command=self.scan_devices
        )
        self.scan_button.pack(pady=(0, 30))

        # Scanning Baud Rate section
        baud_frame = ctk.CTkFrame(device_frame, fg_color="transparent")
        baud_frame.pack(pady=(0, 20))

        baud_label = ctk.CTkLabel(
            baud_frame,
            text="Scanning Baud Rate",
            font=ctk.CTkFont(size=13),
            text_color="#666666"
        )
        baud_label.pack(pady=(0, 10))

        baud_input_frame = ctk.CTkFrame(baud_frame, fg_color="transparent")
        baud_input_frame.pack()

        self.baud_entry = ctk.CTkEntry(
            baud_input_frame,
            width=320,
            height=40,
            corner_radius=8,
            fg_color="#F8F8F8",
            border_width=1,
            border_color="#E0E0E0"
        )
        self.baud_entry.pack(side="left", padx=(0, 10))
        self.baud_entry.insert(0, "115200")

        self.dropdown_button = ctk.CTkButton(
            baud_input_frame,
            text="search",
            width=100,
            height=40,
            corner_radius=6,
            fg_color="#E0E0E0",
            hover_color="#D0D0D0",
            text_color="#666666",
            font=ctk.CTkFont(size=11),
            command=self.show_baud_menu
        )
        self.dropdown_button.pack(side="left")

        # Connect button
        self.connect_button = ctk.CTkButton(
            device_frame,
            text="Connect",
            width=120,
            height=35,
            corner_radius=6,
            fg_color="#2196F3",
            hover_color="#1976D2",
            font=ctk.CTkFont(size=13),
            command=self.connect_device
        )
        self.connect_button.pack(pady=(20, 30))

    def show_baud_menu(self):
        """Show baud rate dropdown menu"""
        menu = ctk.CTkOptionMenu(
            self.scroll_frame,
            values=self.baud_rates,
            command=self.select_baud_rate
        )
        # Position near the button (simplified - in production you'd calculate exact position)
        messagebox.showinfo("Baud Rate", "Select from common baud rates:\n" + "\n".join(self.baud_rates))

    def select_baud_rate(self, rate):
        """Update baud rate entry with selected value"""
        self.baud_entry.delete(0, "end")
        self.baud_entry.insert(0, rate)

    def scan_devices(self):
        """Scan for connected devices"""
        self.device_entry.delete(0, "end")
        self.device_entry.insert(0, "Scanning...")
        self.update()

        # Get list of available COM ports
        ports = serial.tools.list_ports.comports()
        
        if ports:
            port_list = ", ".join([port.device for port in ports])
            self.device_entry.delete(0, "end")
            self.device_entry.insert(0, port_list)
            messagebox.showinfo("Devices Found", f"Found devices:\n{port_list}")
        else:
            self.device_entry.delete(0, "end")
            self.device_entry.insert(0, "No devices found")
            messagebox.showwarning("No Devices", "No serial devices detected")

    def connect_device(self):
        """Connect to the selected device"""
        device = self.device_entry.get()
        baud_rate = self.baud_entry.get()

        if not device or device == "No devices found" or device == "Scanning...":
            messagebox.showerror("Error", "Please scan for devices first")
            return

        if not baud_rate:
            messagebox.showerror("Error", "Please specify a baud rate")
            return

        messagebox.showinfo(
            "Connection",
            f"Connecting to device:\n{device}\nBaud Rate: {baud_rate}"
        )

    def create_system_status_section(self):
        """Create the System Status section with tabs and a data table"""
        # Card container
        section = ctk.CTkFrame(self.scroll_frame, fg_color="white", corner_radius=10)
        section.pack(fill="both", expand=True, pady=(20, 20))

        # Tabs (top segmented control)
        tabs = ctk.CTkTabview(
            section,
            segmented_button_selected_color="#C77DFF",
            segmented_button_selected_hover_color="#B86BEE",
        )
        tabs.pack(fill="x", padx=0, pady=(0, 8))

        tab_names = [
            "Drive Monitoring\nSignals",
            "Current & Voltage\nSignals",
            "Control\nInputs",
            "Speed Loop\nPI Gains",
            "Thermal\nStatus",
            "Can Communication\nStatus",
        ]

        drive_tab = None
        for name in tab_names:
            t = tabs.add(name)
            if name.startswith("Drive Monitoring"):
                drive_tab = t

        # Lavender indicator under tabs (visual cue per mock)
        indicator = ctk.CTkFrame(section, height=4, fg_color="#C77DFF")
        indicator.pack(fill="x")

        # Table like the screenshot
        table_wrap = ctk.CTkFrame(section, fg_color="#F7F7F7")
        table_wrap.pack(padx=20, pady=16, anchor="w")

        table = ctk.CTkFrame(table_wrap, fg_color="white", corner_radius=0)
        table.grid(row=0, column=0, sticky="w")

        rows = [
            "Actual Speed(RPM)",
            "Reference Speed(RPM)",
            "Reference Torque(Nm)",
            "Max Speed Limit(RPM)",
            "Encoder Count",
        ]

        for r, label in enumerate(rows):
            # Left label cell
            left = ctk.CTkFrame(
                table, fg_color="#FFFFFF", corner_radius=0,
                border_width=1, border_color="#CFCFCF"
            )
            left.grid(row=r, column=0, sticky="nsew")
            ctk.CTkLabel(
                left, text=label, text_color="#2D2D2D",
                font=ctk.CTkFont(size=13)
            ).pack(padx=14, pady=10, anchor="w")

            # Right value cell (alternate mint background)
            bg = "#E6F2EA" if r % 2 == 1 else "#FFFFFF"
            right = ctk.CTkFrame(
                table, fg_color=bg, corner_radius=0,
                border_width=1, border_color="#CFCFCF"
            )
            right.grid(row=r, column=1, sticky="nsew")
            ctk.CTkLabel(right, text="", text_color="#2D2D2D").pack(
                padx=14, pady=10, anchor="w"
            )

        # Column widths similar to the mock
        table.grid_columnconfigure(0, minsize=320)
        table.grid_columnconfigure(1, minsize=220)


if __name__ == "__main__":
    app = ePropelledDashboard()
    app.mainloop()
