import gi
import requests  
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango


class AppWindow(Gtk.Window):
    def __init__(self):
        sauper(AppWindow, self).__init__(title="PenGUIn")
        self.set_default_size(1000, 900)

        self.frames_container = Gtk.Box()
        self.add(self.frames_container)
        self.frames_container.show()

        self.main_frame = MainFrame(self)
        self.frames_container.add(self.main_frame)

        self.essential_tweaks = EssentialTweaks(self)
        self.frames_container.add(self.essential_tweaks)
        
        self.advanced_tweaks = AdvancedTweaks(self)
        self.frames_container.add(self.advanced_tweaks)

        self.user_frame = UserFrame(self)
        self.frames_container.add(self.user_frame)

        self.about_frame = AboutFrame(self)
        self.frames_container.add(self.about_frame)

        self.additional_tweaks = AdditionalTweaks(self)
        self.frames_container.add(self.additional_tweaks)

        self.firewall_config_frame = FirewallConfig(self)
        self.frames_container.add(self.firewall_config_frame)

        self.vpn_frame = VPNFrame(self)
        self.frames_container.add(self.vpn_frame)

        self.port_monitoring_frame = PortMonitoring(self)
        self.frames_container.add(self.port_monitoring_frame)

        self.access_and_authentication_frame = AccessAndAuth(self)
        self.frames_container.add(self.access_and_authentication_frame)

        self.rbac_frame = RoleBasedAccessControl(self)
        self.frames_container.add(self.rbac_frame)
        
    def setup_side_menu(self, frame, main_content):
        frame.paned = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        frame.add(frame.paned)
        
        frame.side_menu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        side_menu_style = frame.side_menu.get_style_context()
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"box { background-color: #252525; }")
        side_menu_style.add_provider(css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        
        buttons_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        buttons_container.set_margin_top(235)
        buttons_container.set_margin_start(20)
        buttons_container.set_margin_end(20)
        
        home_button = Gtk.Button(label="Home")
        home_button.connect("clicked", lambda __: self.switch_to_main_frame())
        essential_button = Gtk.Button(label="Essential Tweaks")
        essential_button.connect("clicked", lambda __: self.switch_to_essential_tweaks())
        advanced_button = Gtk.Button(label="Advanced Tweaks")
        advanced_button.connect("clicked", lambda __: self.switch_to_advanced_tweaks())
        additional_button = Gtk.Button(label="Additional Tweaks")
        additional_button.connect("clicked", lambda __: self.switch_to_additional_tweaks())
        system_info_button = Gtk.Button(label="System Info")
        user_button = Gtk.Button(label="User")
        user_button.connect("clicked", lambda __: self.switch_to_user_frame())
        about_button = Gtk.Button(label="About")
        about_button.connect("clicked", lambda __: self.switch_to_about_frame())

        for button in [home_button, essential_button, advanced_button, additional_button, system_info_button, user_button, about_button]:
            button.set_size_request(100, 35)
        
        buttons_container.pack_start(home_button, False, False, 0)
        buttons_container.pack_start(essential_button, False, False, 0)
        buttons_container.pack_start(advanced_button, False, False, 0)
        buttons_container.pack_start(additional_button, False, False, 0)
        buttons_container.pack_start(system_info_button, False, False, 0)
        buttons_container.pack_start(user_button, False, False, 0)
        buttons_container.pack_start(about_button, False, False, 0)
        
        frame.side_menu.pack_start(buttons_container, False, False, 0)
        frame.paned.pack1(frame.side_menu, resize=True, shrink=False)
        frame.paned.pack2(main_content, resize=True, shrink=False)
        frame.paned.set_position(200)
    
    def switch_to_main_frame(self):
        self.essential_tweaks.hide()
        self.advanced_tweaks.hide()
        self.user_frame.hide()
        self.about_frame.hide()
        self.additional_tweaks.hide()
        self.firewall_config_frame.hide()
        self.vpn_frame.hide()
        self.port_monitoring_frame.hide()
        self.access_and_authentication_frame.hide()
        self.rbac_frame.hide()
        self.main_frame.show_all()

    def switch_to_essential_tweaks(self):
        self.advanced_tweaks.hide()
        self.user_frame.hide()
        self.about_frame.hide()
        self.additional_tweaks.hide()
        self.firewall_config_frame.hide()
        self.vpn_frame.hide()
        self.port_monitoring_frame.hide()
        self.access_and_authentication_frame.hide()
        self.rbac_frame.hide()
        self.main_frame.hide()
        self.essential_tweaks.show_all()

    def switch_to_advanced_tweaks(self):
        self.user_frame.hide()
        self.about_frame.hide()
        self.additional_tweaks.hide()
        self.firewall_config_frame.hide()
        self.vpn_frame.hide()
        self.port_monitoring_frame.hide()
        self.access_and_authentication_frame.hide()
        self.rbac_frame.hide()
        self.main_frame.hide()
        self.essential_tweaks.hide()
        self.advanced_tweaks.show_all()

    def switch_to_user_frame(self):
        self.about_frame.hide()
        self.additional_tweaks.hide()
        self.firewall_config_frame.hide()
        self.vpn_frame.hide()
        self.port_monitoring_frame.hide()
        self.access_and_authentication_frame.hide()
        self.rbac_frame.hide()
        self.main_frame.hide()
        self.essential_tweaks.hide()
        self.advanced_tweaks.hide()
        self.user_frame.show_all()

    def switch_to_about_frame(self):
        self.additional_tweaks.hide()
        self.firewall_config_frame.hide()
        self.vpn_frame.hide()
        self.port_monitoring_frame.hide()
        self.access_and_authentication_frame.hide()
        self.rbac_frame.hide()
        self.main_frame.hide()
        self.essential_tweaks.hide()
        self.advanced_tweaks.hide()
        self.user_frame.hide()
        self.about_frame.show_all()

    def switch_to_additional_tweaks(self):
        self.firewall_config_frame.hide()
        self.vpn_frame.hide()
        self.port_monitoring_frame.hide()
        self.access_and_authentication_frame.hide()
        self.rbac_frame.hide()
        self.main_frame.hide()
        self.essential_tweaks.hide()
        self.advanced_tweaks.hide()
        self.user_frame.hide()
        self.about_frame.hide()
        self.additional_tweaks.show_all()



class MainFrame(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window
        
        self.layout = Gtk.Layout()
        layout_container = Gtk.Box()
        layout_container.set_size_request(800, 600)
        layout_container.pack_start(self.layout, True, True, 0)
        
        parent_window.setup_side_menu(self, layout_container)
        
        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>PenGUIn</b></span>")
        self.layout.put(label, 270, 90)

        # Main default mode
        main_essential_tweaks = Gtk.Button()
        main_essential_tweaks.connect("clicked", lambda _: self.switch_to_essential_tweaks())
        essential_label = Gtk.Label(label="ESSENTIAL TWEAKS")
        essential_label.set_use_markup(True)
        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)
        essential_label.set_attributes(attr_list)
        main_essential_tweaks.add(essential_label)
        main_essential_tweaks.set_size_request(100, 75)
        self.layout.put(main_essential_tweaks, 70, 300)

        # Default paragraph
        default_paragraph = Gtk.Label()
        default_paragraph.set_markup("In-Built Solutions to\nYour Security Needs")
        default_paragraph.set_use_markup(True)
        paragraph_attr_list = Pango.AttrList()
        paragraph_attr = Pango.AttrSize.new(16000)
        paragraph_attr_list.insert(paragraph_attr)
        default_paragraph.set_attributes(paragraph_attr_list)
        default_paragraph.set_justify(Gtk.Justification.CENTER)
        self.layout.put(default_paragraph, 105, 400)

        # Main advanced mode
        main_advanced_tweaks = Gtk.Button()
        main_advanced_tweaks.connect("clicked", lambda _: self.switch_to_advanced_frame())
        advanced_label = Gtk.Label(label="ADVANCED TWEAKS")
        advanced_label.set_use_markup(True)
        advanced_label.set_attributes(attr_list)
        main_advanced_tweaks.add(advanced_label)
        main_advanced_tweaks.set_size_request(100, 75)
        self.layout.put(main_advanced_tweaks, 430, 300)

        # Advanced paragraph
        advanced_paragraph = Gtk.Label()
        advanced_paragraph.set_markup("Customizable Solutions to\nYour Security Needs")
        advanced_paragraph.set_use_markup(True)
        advanced_paragraph.set_attributes(paragraph_attr_list)
        advanced_paragraph.set_justify(Gtk.Justification.CENTER)
        self.layout.put(advanced_paragraph, 440, 400)

        # Main Add Ons
        main_additional_tweaks = Gtk.Button()
        main_additional_tweaks.connect("clicked", lambda _: self.switch_to_additional_tweaks())
        additional_label = Gtk.Label(label="ADDITIONAL TWEAKS")
        additional_label.set_use_markup(True)
        additional_label.set_attributes(attr_list)
        main_additional_tweaks.add(additional_label)
        main_additional_tweaks.set_size_request(100, 75)
        self.layout.put(main_additional_tweaks, 240, 520)

        # Add Ons paragraph
        add_ons_paragraph = Gtk.Label()
        add_ons_paragraph.set_markup("Additional Solutions to\nYour Security Needs")
        add_ons_paragraph.set_attributes(paragraph_attr_list)
        add_ons_paragraph.set_justify(Gtk.Justification.CENTER)
        self.layout.put(add_ons_paragraph, 265, 620)
       

    def switch_to_essential_tweaks(self):
        self.__parent_window.essential_tweaks.show_all()
        self.hide()
        
    def switch_to_advanced_frame(self):
        self.__parent_window.advanced_tweaks.show_all()
        self.hide()

    def switch_to_additional_tweaks(self):
        self.__parent_window.additional_tweaks.show_all()
        self.hide()


class EssentialTweaks(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window
        
        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)
        
        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)

        attr_list2 = Pango.AttrList()  # Pango attributes
        attr2 = Pango.AttrSize.new(15000)
        attr_list2.insert(attr2)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>ESSENTIAL TWEAKS</b></span>")
        self.fix.put(label, 115, 90)
        
        firewall_button = Gtk.Button()
        firewall_button.set_size_request(325,70)
        firewall_label = Gtk.Label(label="Low Essential Tweaks")
        firewall_label.set_use_markup(True)
        firewall_label.set_attributes(attr_list)
        firewall_button.add(firewall_label)
        firewall_button.connect("clicked", self.on_low_essential_tweaks_clicked)
        self.fix.put(firewall_button,45,300)
        
        remote_access_button = Gtk.Button()
        remote_access_button.set_size_request(325,70)
        remote_label = Gtk.Label(label="Medium Essential Tweaks")
        remote_label.set_use_markup(True)
        remote_label.set_attributes(attr_list)
        remote_access_button.add(remote_label)
        remote_button.connect("clicked", self.on_medium_essential_tweaks_clicked)
        self.fix.put(remote_access_button,405,300)
        
        return_button = Gtk.Button()
        return_button.set_size_request(150,50)
        return_label = Gtk.Label(label = "Back")
        return_button.connect("clicked", lambda _: self.return_main_frame())
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list2)
        return_button.add(return_label)
        self.fix.put(return_button,300,500)
        
    def on_low_essential_tweaks_clicked(self, widget):
   
        subprocess.run(["chmod", "+x", "lowtweaks.sh"])
        subprocess.run(["gnome-terminal", "--", "bash", lowtweaks.sh])

    def on_medium_essential_tweaks_clicked(self, widget):
        
        subprocess.run(["chmod", "+x", "mediumtweaks.sh"])
        subprocess.run(["gnome-terminal", "--", "bash", mediumtweaks.sh])


    def return_main_frame(self):
        self.__parent_window.main_frame.show_all()
        self.hide()
        
        
class AdvancedTweaks(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)

        attr_list = Pango.AttrList()
        attr = Pango.AttrSize.new(15000)
        attr_list.insert(attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>ADVANCED TWEAKS</b></span>")
        self.fix.put(label, 115, 90)

        firewall_button = Gtk.Button()
        firewall_button.set_size_request(225,70)
        firewall_button.connect("clicked", lambda _: self.reach_firewall_config())
        firewall_label = Gtk.Label(label="Firewall Configuration")
        firewall_label.set_use_markup(True)
        firewall_label.set_attributes(attr_list)
        firewall_button.add(firewall_label)
        self.fix.put(firewall_button,285,200)

        vpn_button = Gtk.Button()
        vpn_button.set_size_request(225,70)
        vpn_button.connect("clicked", lambda _: self.reach_vpn_frame())
        vpn_label = Gtk.Label(label="VPN")
        vpn_label.set_use_markup(True)
        vpn_label.set_attributes(attr_list)
        vpn_button.add(vpn_label)
        self.fix.put(vpn_button,285,300)

        port_monitoring_button = Gtk.Button()
        port_monitoring_button.set_size_request(225,70)
        port_monitoring_button.connect("clicked", lambda _: self.reach_port_monitoring_frame())
        port_monitoring_label = Gtk.Label(label="Port Monitoring")
        port_monitoring_label.set_use_markup(True)
        port_monitoring_label.set_attributes(attr_list)
        port_monitoring_button.add(port_monitoring_label)
        self.fix.put(port_monitoring_button,285,400)

        access_and_authentication_button = Gtk.Button()
        access_and_authentication_button.set_size_request(225,70)
        access_and_authentication_button.connect("clicked", lambda _: self.reach_access_and_auth_frame())
        access_and_authentication_label = Gtk.Label(label="Access and Authentication Centre")
        access_and_authentication_label.set_use_markup(True)
        access_and_authentication_label.set_attributes(attr_list)
        access_and_authentication_button.add(access_and_authentication_label)
        self.fix.put(access_and_authentication_button,225,500)

        aide_button = Gtk.Button()
        aide_button.set_size_request(225, 70)
        aide_label = Gtk.Label(label="AIDE")
        aide_label.set_use_markup(True)
        aide_label.set_attributes(attr_list)
        aide_button.add(aide_label)
        aide_button.connect("clicked", self.on_aide_button_clicked)
        self.fix.put(aide_button, 285, 600)

        return_button = Gtk.Button()
        return_button.set_size_request(150, 50)
        return_button.connect("clicked", lambda _: self.return_main_frame())
        return_label = Gtk.Label(label="Back")
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list)
        return_button.add(return_label)
        self.fix.put(return_button, 320, 750)
        
    def return_main_frame(self):
        self.__parent_window.main_frame.show_all()
        self.hide()

    def reach_firewall_config(self):
        self.__parent_window.firewall_config_frame.show_all()
        self.hide()

    def reach_vpn_frame(self):
        self.__parent_window.vpn_frame.show_all()
        self.hide()

    def reach_port_monitoring_frame(self):
        self.__parent_window.port_monitoring_frame.show_all()
        self.hide()

    def reach_access_and_auth_frame(self):
        self.__parent_window.access_and_authentication_frame.show_all()
        self.hide()

    def on_aide_button_clicked(self, widget):
        chmod_command = ["chmod", "+x", "aide.sh"]
        subprocess.run(chmod_command, check=True)
        subprocess.run(["sudo", "aide.sh"])

    

class UserFrame(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window #Not Necessary

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)
        
        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>Hi! PenGUIn User!</b></span>")
        self.fix.put(label, 150, 90)

        user_name = Gtk.Label()
        user_name.set_markup("<span size='20000'><b>Name : </b></span>")
        self.fix.put(user_name, 150, 350)

        user_name_entry = Gtk.Entry()
        user_name_entry.set_text("Name of the User")
        user_name_entry.set_size_request(350, 35)
        user_name_entry.set_editable(False)
        #user_name_entry.set_sensitive(False)
        self.fix.put(user_name_entry, 275, 350)

        email_id = Gtk.Label()
        email_id.set_markup("<span size='20000'><b>Email ID : </b></span>")
        self.fix.put(email_id, 150, 400)

        email_entry = Gtk.Entry()
        email_entry.set_text("Email Address")
        email_entry.set_size_request(300, 35)
        email_entry.set_editable(False)
        self.fix.put(email_entry, 322, 400)

        attr_list = Pango.AttrList()
        attr = Pango.AttrSize.new(15000)
        attr_list.insert(attr)

        log_out_button = Gtk.Button()
        log_out_button.set_size_request(150, 50)
        log_out_label = Gtk.Label(label="LOG OUT")
        log_out_label.set_use_markup(True)
        log_out_label.set_attributes(attr_list)
        log_out_button.add(log_out_label)
        self.fix.put(log_out_button, 320, 550)

class AboutFrame(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window    #Not Necessary

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)

        paragraph_attr_list = Pango.AttrList()
        paragraph_attr = Pango.AttrSize.new(15000)
        paragraph_attr_list.insert(paragraph_attr)
        paragraph_attr_list.insert(paragraph_attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>About PenGUIn</b></span>")
        self.fix.put(label, 195, 90)

        section_one_label = Gtk.Label()
        section_one_label.set_markup("<span size='25000'><b>Simplified OS Hardening</b></span>")
        self.fix.put(section_one_label, 195, 175)

        section_one_paragraph = Gtk.Label()
        section_one_paragraph.set_markup("Discover a user-friendly Linux app with a GUI that simplifies OS hardening.\nSay goodbye to complex scripts and secure your system effortlessly.")
        section_one_paragraph.set_attributes(paragraph_attr_list)
        section_one_paragraph.set_justify(Gtk.Justification.CENTER)
        self.fix.put(section_one_paragraph, 47, 250) 

        section_two_label = Gtk.Label()
        section_two_label.set_markup("<span size='25000'><b>Tailored Security Options</b></span>")
        self.fix.put(section_two_label, 195, 335)

        section_two_paragraph = Gtk.Label()
        section_two_paragraph.set_markup("Choose from Default, Advanced, and add-on options to meet\nyour specific security needs.\nOur modular design allows you to customize your protection.")
        section_two_paragraph.set_attributes(paragraph_attr_list)
        section_two_paragraph.set_justify(Gtk.Justification.CENTER)
        self.fix.put(section_two_paragraph,125, 410)

        section_three_label = Gtk.Label()
        section_three_label.set_markup("<span size='25000'><b>Key Features</b></span>")
        self.fix.put(section_three_label, 285, 520)

        section_three_paragraph = Gtk.Label()
        section_three_paragraph.set_markup("Block SSH, TOR, and USB ports with ease.\nStreamlined USB blocking with a single click.\nSecure your network by blocking Tor Exit nodes using Iptables.")
        section_three_paragraph.set_attributes(paragraph_attr_list)
        section_three_paragraph.set_justify(Gtk.Justification.CENTER)
        self.fix.put(section_three_paragraph, 100, 600)

class AdditionalTweaks(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window    #Not Necessary

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)

        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>ADDITIONAL TWEAKS</b></span>")
        self.fix.put(label, 100, 90)
        
        cache_cleaning_button = Gtk.Button()
        cache_cleaning_button.set_size_request(325,70)
        cache_cleaning_label = Gtk.Label(label="CLEAN CACHE")
        cache_cleaning_label.set_use_markup(True)
        cache_cleaning_label.set_attributes(attr_list)
        cache_cleaning_button.add(cache_cleaning_label)
        cache_cleaning_button.connect("clicked", self.on_cache_cleaning_button_clicked)
        self.fix.put(cache_cleaning_button,240,250)
        
        temp_file_button = Gtk.Button()
        temp_file_button.set_size_request(325,70)
        temp_file_label = Gtk.Label(label="CLEAN TEMPORARY FILES")
        temp_file_label.set_use_markup(True)
        temp_file_label.set_attributes(attr_list)
        temp_file_button.add(temp_file_label)
        temp_file_label.connect("clicked" , self.on_temp_files_clean)
        self.fix.put(temp_file_button,220,400) 

        update_checker_button = Gtk.Button()
        update_checker_button.set_size_request(325,70)
        update_checker_label = Gtk.Label(label="UPDATE CHECKER")
        update_checker_label.set_use_markup(True)
        update_checker_label.set_attributes(attr_list)
        update_checker_button.add(update_checker_label)
        update_checker_button.connect("clicked" , self.on_updates_clicked)
        self.fix.put(update_checker_button,240,550)

        return_button = Gtk.Button()
        return_button.set_size_request(150, 50)
        return_button.connect("clicked", lambda _: self.return_main_frame())
        return_label = Gtk.Label(label="Back")
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list)
        return_button.add(return_label)
        self.fix.put(return_button, 320, 700)
        
    def return_main_frame(self):
        self.__parent_window.main_frame.show_all()
        self.hide()

    def on_temp_files_clean(self , widget):
           chmod_command = ["chmod", "+x", "tempfiles.sh"]
           subprocess.run(chmod_command, check=True)
           subprocess.run(["tempfiles.sh"])
       


    def on_cache_cleaning_button_clicked(self, widget):
            chmod_command = ["chmod", "+x", "clearcache.sh"]
            subprocess.run(chmod_command, check=True)
            subprocess.run(["clearcache.sh"])
        
    def on_updates_clicked(self , widget):
           chmod_command = ["chmod", "+x", "updates.sh"]
           subprocess.run(chmod_command, check=True)
           subprocess.run(["updates.sh"])

class FirewallConfig(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window 

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)

        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='35000'><b>FIREWALL CONFIGURATION</b></span>")
        self.fix.put(label, 50, 90)
        
        blocking_tor_button = Gtk.Button()
        blocking_tor_button.set_size_request(325,70)
        blocking_tor_label = Gtk.Label(label="Block TOR")
        blocking_tor_label.set_use_markup(True)
        blocking_tor_label.set_attributes(attr_list)
        blocking_tor_button.add(blocking_tor_label)
        blocking_tor_button.connect("clicked", self.configure_tor_blocking)
        self.fix.put(blocking_tor_button,240,250)

        rule_management_button = Gtk.Button()
        rule_management_button.set_size_request(325,70)
        rule_management_label = Gtk.Label(label="Rule Management")
        rule_management_label.set_use_markup(True)
        rule_management_label.set_attributes(attr_list)
        rule_management_button.add(rule_management_label)
        rule_management_button.connect("clicked", self.run_rule_management_script)
        self.fix.put(rule_management_button,240, 350)

        white_listing_button = Gtk.Button()
        white_listing_button.set_size_request(325,70)
        white_listing_label = Gtk.Label(label="White Listing")
        white_listing_label.set_use_markup(True)
        white_listing_label.set_attributes(attr_list)
        white_listing_button.add(white_listing_label)
        white_listing_button.connect("clicked", self.open_whitelisting_script)
        self.fix.put(white_listing_button,240,450)

        trusted_users_button = Gtk.Button()
        trusted_users_button.set_size_request(325,70)
        trusted_users_label = Gtk.Label(label="Setting Trusted Users")
        trusted_users_label.set_use_markup(True)
        trusted_users_label.set_attributes(attr_list)
        trusted_users_button.add(trusted_users_label)
        trusted_users_button.connect("clicked" , self.only_trusted_users)
        self.fix.put(trusted_users_button,240,550)

        url_filtering_button = Gtk.Button()
        url_filtering_button.set_size_request(325,70)
        url_filtering_label = Gtk.Label(label="URL Filtering")
        url_filtering_label.set_use_markup(True)
        url_filtering_label.set_attributes(attr_list)
        url_filtering_button.add(url_filtering_label)
        self.fix.put(url_filtering_button,240,650)

        return_button = Gtk.Button()
        return_button.set_size_request(150, 50)
        return_button.connect("clicked", lambda _: self.return_advanced_frame())
        return_label = Gtk.Label(label="Back")
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list)
        return_button.add(return_label)
        self.fix.put(return_button, 320, 800)

    

    def run_rule_management_script(self, widget):
        subprocess.run(["chmod", "+x", "rulemanagement.sh"])
        subprocess.run(["gnome-terminal", "--", "bash", "rulemanagement.sh"])



    def configure_tor_blocking(self, widget):
        subprocess.run(["chmod", "+x", "blockingtor.sh"])
        subprocess.run(["gnome-terminal", "--", "bash", "blockingtor.sh"])


    def open_whitelisting_script(self, widget):
        subprocess.run(["chmod", "+x", "whitelisting.sh"])
        subprocess.run(["gnome-terminal", "--", "bash", "whitelisting.sh"])
    
    def only_trusted_users(self, widget):
         subprocess.run(["chmod", "+x", "trustedusers.sh"])
         subprocess.run(["gnome-terminal", "--", "bash", "trustedusers.sh"])
       
     

    def return_advanced_frame(self):
        self.__parent_window.advanced_tweaks.show_all()
        self.hide()



class VPNFrame(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window    

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)

        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>VPN CONFIGURATION</b></span>")
        self.fix.put(label, 85, 90)
        
        view_status_button = Gtk.Button()
        view_status_button.set_size_request(325,70)
        view_status_label = Gtk.Label(label="View Status")
        view_status_label.set_use_markup(True)
        view_status_label.set_attributes(attr_list)
        view_status_button.add(view_status_label)
        view_status_button.connect("clicked", self.open_vpn_status)
        self.fix.put(view_status_button,55,350)

        view_config_button = Gtk.Button()
        view_config_button.set_size_request(325,70)
        view_config_label = Gtk.Label(label="View Configuration File")
        view_config_label.set_use_markup(True)
        view_config_label.set_attributes(attr_list)
        view_config_button.add(view_config_label)
        view_config_button.connect("clicked", self.view_config_file)
        self.fix.put(view_config_button,55,450)

        vpn_label = Gtk.Label()
        vpn_label.set_markup("<span size='16000'><b>Enable/Disable VPN</b></span>")
        self.fix.put(vpn_label, 445, 425)

        vpn_switch = Gtk.Switch()
        vpn_switch.set_size_request(80, 35)
        vpn_switch.connect("notify::active", self.on_vpn_switch_activated)
        vpn_switch.set_active(False)
        self.fix.put(vpn_switch, 685, 420)

        return_button = Gtk.Button()
        return_button.set_size_request(150, 50)
        return_button.connect("clicked", lambda _: self.return_advanced_frame())
        return_label = Gtk.Label(label="Back")
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list)
        return_button.add(return_label)
        self.fix.put(return_button, 320, 700)
         
        self.add(self.fix)

    def on_vpn_switch_activated(self, switch, gparam):
        if switch.get_active():
            self.enable_wireguard_vpn()
        else:
            self.disable_wireguard_vpn()

    def enable_wireguard_vpn(self):
        vpn_interface = "wg0"  # Replace with your WireGuard VPN interface name
        self.run_wireguard_script(vpn_interface)

    def disable_wireguard_vpn(self):
        vpn_interface = "wg0"  # Replace with your WireGuard VPN interface name
        self.run_wireguard_script(vpn_interface)

    def run_wireguard_script(self, vpn_interface):
        vpn_interface = "wg0" 
        subprocess.run(["chmod", "+x", "toggle_vpn.sh"])
        subprocess.run(["sudo", "toggle_vpn.sh", vpn_interface], check=True)
        

    def return_advanced_frame(self):
        self.__parent_window.advanced_tweaks.show_all()
        self.hide()

    def enable_or_disable_vpn(self, switch):
        if switch.get_active():
            state = True
        else:
            state = False
        print("VPN Status: " , state)


    def open_vpn_status():
         subprocess.run(["chmod", "+x", "vpn.sh"])
         subprocess.run(["gnome-terminal", "--", "bash", vpn.sh])

    def view_config_file(self, widget):
        script_path = "configvpn.sh"
        config_file_path = "/etc/wireguard/<your-config-file>.conf"
        chmod_command = ["chmod", "+x", script_file]
        subprocess.run(chmod_command, check=True)
        subprocess.run(["bash", script_path, config_file_path])    


class PortMonitoring(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window 

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)

        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='40000'><b>PORT MONITORING</b></span>")
        self.fix.put(label, 115, 90)
        
        ssh_hardening_button = Gtk.Button()
        ssh_hardening_button.set_size_request(325,70)
        ssh_hardening_label = Gtk.Label(label="Block SSH")
        ssh_hardening_label.set_use_markup(True)
        ssh_hardening_label.set_attributes(attr_list)
        ssh_hardening_button.add(ssh_hardening_label)
        ssh_hardening_button.connect("clicked", self.block_ssh_traffic)
        self.fix.put(ssh_hardening_button,240,250)

        usb_port_control_button = Gtk.Button()
        usb_port_control_button.set_size_request(325,70)
        usb_port_control_label = Gtk.Label(label="Control USB Ports")
        usb_port_control_label.set_use_markup(True)
        usb_port_control_label.set_attributes(attr_list)
        usb_port_control_button.add(usb_port_control_label)
        usb_port_control_button.connect("clicked", self.on_usb_port_control_button_clicked)
        self.fix.put(usb_port_control_button,240,350)

        sftp_harden_button = Gtk.Button()
        sftp_harden_button.set_size_request(325,70)
        sftp_harden_label = Gtk.Label(label="Harden SFTP")
        sftp_harden_label.set_use_markup(True)
        sftp_harden_label.set_attributes(attr_list)
        sftp_harden_button.add(sftp_harden_label)
        sftp_harden_button.connect("clicked", self.sftp_hardening)
        self.fix.put(sftp_harden_button,240,450)

        view_log_button = Gtk.Button()
        view_log_button.set_size_request(325,70)
        view_log_label = Gtk.Label(label="View LOGs")
        view_log_label.set_use_markup(True)
        view_log_label.set_attributes(attr_list)
        view_log_button.add(view_log_label)
        view_log_button.connect("clicked", self.on_view_logs_button_clicked)
        self.fix.put(view_log_button,240,550)

        return_button = Gtk.Button()
        return_button.set_size_request(150, 50)
        return_button.connect("clicked", lambda _: self.return_advanced_frame())
        return_label = Gtk.Label(label="Back")
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list)
        return_button.add(return_label)
        self.fix.put(return_button, 320, 700)

    def return_advanced_frame(self):
        self.__parent_window.advanced_tweaks.show_all()
        self.hide()

    def block_ssh_traffic(self, widget):
        chmod_command = ["chmod", "+x", script_path]
        subprocess.run(chmod_command, check=True)
        subprocess.run(["sudo", "bash", "blockingssh.sh"], check=True)
        print("SSH blocking script executed successfully!")
       

    def on_usb_port_control_button_clicked(self, widget):
        chmod_command = ["chmod", "+x", "usbports.sh"]
        subprocess.run(chmod_command, check=True)
        subprocess.run(["sudo", "bash", "usbports.sh"])

    def sftp_hardening():
        chmod_command = ["chmod", "+x", "sftp.sh"]
        subprocess.run(chmod_command, check=True)
        subprocess.run(["sudo", "bash", "sftp.sh"])

    
    def on_view_logs_button_clicked(self, widget):
        chmod_command = ["chmod", "+x", "logs.sh"]
        subprocess.run(chmod_command, check=True)
        subprocess.run(["logs.sh"])
        with open("system_logs.txt", "r") as log_file:
            log_content = log_file.read()


    

class AccessAndAuth(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window

        self.fix = Gtk.Fixed()
        
        parent_window.setup_side_menu(self, self.fix)

        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='35000'><b>ACCESS AND AUTHENTICATION\nCENTRE</b></span>")
        label.set_justify(Gtk.Justification.CENTER)
        self.fix.put(label, 10, 90)

        twofa_button = Gtk.Button()
        twofa_button.set_size_request(325,70)
        twofa_label = Gtk.Label(label="2FA SETUP")
        twofa_label.set_use_markup(True)
        twofa_label.set_attributes(attr_list)
        twofa_button.add(twofa_label)
        self.fix.put(twofa_button,240,250)

        password_config_button = Gtk.Button()
        password_config_button.set_size_request(325,70)
        password_config_label = Gtk.Label(label="Password Configuration")
        password_config_label.set_use_markup(True)
        password_config_label.set_attributes(attr_list)
        password_config_button.add(password_config_label)
        self.fix.put(password_config_button,240,350)

        lockout_policy_button = Gtk.Button()
        lockout_policy_button.set_size_request(325,70)
        lockout_policy_label = Gtk.Label(label="Lockout Policy")
        lockout_policy_label.set_use_markup(True)
        lockout_policy_label.set_attributes(attr_list)
        lockout_policy_button.add(lockout_policy_label)
        self.fix.put(lockout_policy_button,240,450)

        rbac_button = Gtk.Button()
        rbac_button.set_size_request(325,70)
        rbac_button.connect("clicked", lambda _: self.reach_role_based_access_control_frame())
        rbac_label = Gtk.Label(label="Role Based Access Control")
        rbac_label.set_use_markup(True)
        rbac_label.set_attributes(attr_list)
        rbac_button.add(rbac_label)
        self.fix.put(rbac_button,220,550)

        return_button = Gtk.Button()
        return_button.set_size_request(150, 50)
        return_button.connect("clicked", lambda _: self.return_advanced_frame())
        return_label = Gtk.Label(label="Back")
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list)
        return_button.add(return_label)
        self.fix.put(return_button, 320, 700)

    def return_advanced_frame(self):
        self.__parent_window.advanced_tweaks.show_all()
        self.hide()

    def reach_role_based_access_control_frame(self):
        self.__parent_window.rbac_frame.show_all()
        self.hide()

class RoleBasedAccessControl(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window

        self.fix = Gtk.Fixed()

        parent_window.setup_side_menu(self, self.fix)

        attr_list = Pango.AttrList()  # Pango attributes
        attr = Pango.AttrSize.new(20000)
        attr_list.insert(attr)

        label = Gtk.Label()  # Main title
        label.set_markup("<span size='35000'><b>ROLE BASED\nACCESS CONTROL</b></span>")
        label.set_justify(Gtk.Justification.CENTER)
        self.fix.put(label, 170, 90)

        role_label = Gtk.Label()
        role_label.set_markup("<span size = '25000'><b>Role: </b></span>")
        self.fix.put(role_label, 90, 250)

        roles = ["Choose a Role", "Role 1", "Role 2", "Role 3", "Role 4", "Role 5"]
        roles_list_dropdown_box = Gtk.ComboBoxText()
        roles_list_dropdown_box.set_size_request(250, 50)
        for role in roles:
            roles_list_dropdown_box.append_text(role)
        roles_list_dropdown_box.connect("changed", self.role_changed)
        roles_list_dropdown_box.set_active(0)
        self.fix.put(roles_list_dropdown_box, 210, 245)

        add_button = Gtk.Button()
        add_button.set_size_request(50, 50)
        add_label = Gtk.Label(label="+")
        add_label.set_use_markup(True)
        add_label.set_attributes(attr_list)
        add_button.add(add_label)
        self.fix.put(add_button, 485, 245)

        remove_button = Gtk.Button()
        remove_button.set_size_request(50, 50)
        remove_label = Gtk.Label(label="-")
        remove_label.set_use_markup(True)
        remove_label.set_attributes(attr_list)
        remove_button.add(remove_label)
        self.fix.put(remove_button, 550, 245)

        permissions_label = Gtk.Label()
        permissions_label.set_markup("<span size = '25000'><b>Permissions: </b></span>")
        self.fix.put(permissions_label, 90, 340)

        sample_button = Gtk.RadioButton.new_with_label_from_widget(None, "Sample")

        create_button = Gtk.RadioButton.new_from_widget(sample_button)
        create_button.set_label("Create")
        create_button.connect("toggled", self.on_button_toggled, "create")
        self.fix.put(create_button,  350, 345)

        read_button = Gtk.RadioButton.new_from_widget(sample_button)
        read_button.set_label("Read")
        read_button.connect("toggled", self.on_button_toggled, "read")
        self.fix.put(read_button,  450, 345)

        update_button = Gtk.RadioButton.new_from_widget(sample_button)
        update_button.set_label("Update")
        update_button.connect("toggled", self.on_button_toggled, "update")
        self.fix.put(update_button,  350, 390)

        delete_button = Gtk.RadioButton.new_from_widget(sample_button)
        delete_button.set_label("Delete")
        delete_button.connect("toggled", self.on_button_toggled, "delete")
        self.fix.put(delete_button,  450, 390)

        access_list = Gtk.Label()
        access_list.set_markup("<span size='25000'><b>Access Control\nLists : </b></span>")
        self.fix.put(access_list, 90, 460)

        access_entry = Gtk.Entry()
        access_entry.set_size_request(300, 100)
        self.fix.put(access_entry, 375, 455)

        submit_button = Gtk.Button()
        submit_button.set_size_request(150, 50)
        submit_label = Gtk.Label(label="Submit")
        submit_label.set_use_markup(True)
        submit_label.set_attributes(attr_list)
        submit_button.add(submit_label)
        self.fix.put(submit_button, 100, 600)

        upload_button = Gtk.Button()
        upload_button.set_size_request(150, 50)
        upload_label = Gtk.Label(label="Upload Configuration File")
        upload_label.set_use_markup(True)
        upload_label.set_attributes(attr_list)
        upload_button.add(upload_label)
        self.fix.put(upload_button, 325, 600)

        return_button = Gtk.Button()
        return_button.set_size_request(150, 50)
        return_button.connect("clicked", lambda _: self.return_access_and_auth_frame())
        return_label = Gtk.Label(label="Back")
        return_label.set_use_markup(True)
        return_label.set_attributes(attr_list)
        return_button.add(return_label)
        self.fix.put(return_button, 320, 700)


    def return_access_and_auth_frame(self):
        self.__parent_window.access_and_authentication_frame.show_all()
        self.hide()

    def role_changed(self, combo):
        active_text = combo.get_active_text()
        #if active_text is not None:
            #print("Selected Role:", active_text)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        #print("Button", name, "was turned", state)








if __name__ == '__main__':
    window = AppWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.main_frame.show_all()
    window.show()
    Gtk.main()


'''
1. Simplified OS Hardening

Discover a user-friendly Linux app with a GUI that simplifies OS hardening. Say goodbye to complex scripts and secure your system effortlessly.

2. Tailored Security Options

Choose from Default, Advanced, and add-on options to meet your specific security needs. Our modular design allows you to customize your protection.

3. Key Features

Block SSH, TOR, and USB ports with ease.
Streamlined USB blocking with a single click.
Secure your network by blocking Tor Exit nodes using Iptables.'''
