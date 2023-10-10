%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A privacy-respecting, open source and secure TV ecosystem
Name:		plasma-bigscreen
Version:	5.27.8
Release:	2
License:	LGPL
Group:		System/Libraries
Url:		http://plasma-bigscreen.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5ActivitiesStats)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(LibKWorkspace) < 5.27.50
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(PlasmaWaylandProtocols) >= 1.4.0
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	qt5-qtwayland
BuildRequires:	qml(org.kde.plasma.core)
Requires:	qml(org.kde.plasma.core)
Requires:	%{name}-frontend = %{EVRD}

%description
A privacy-respecting, open source and secure TV ecosystem.

%package wayland
Summary:	Wayland support for plasma-bigscreen
Provides:	%{name}-frontend = %{EVRD}
Requires:	%{name} = %{EVRD}

%description wayland
Wayland support for plasma-bigscreen

%files wayland
%{_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop
%{_bindir}/plasma-bigscreen-wayland


%package x11
Summary:	X11 support for plasma-bigscreen
Requires:	%{name} = %{EVRD}

%description x11
X11 support for plasma-bigscreen.

%files x11
%{_datadir}/xsessions/plasma-bigscreen-x11.desktop
%{_bindir}/plasma-bigscreen-x11


%files -f %{name}.lang
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen
%{_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi
%{_datadir}/metainfo/org.kde.mycroft.bigscreen.homescreen.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mycroft.bigscreen.metainfo.xml
%{_datadir}/metainfo/org.kde.plasma.mycroft.bigscreen.appdata.xml
%{_datadir}/kservices5/plasma-lookandfeel-org.kde.plasma.mycroft.bigscreen.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.mycroft.bigscreen.homescreen.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.mycroft.bigscreen.desktop
%{_datadir}/sounds/plasma-bigscreen
%{_bindir}/mycroft-skill-launcher.py
%{_libdir}/qt5/qml/org/kde/mycroft
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_biglauncherhomescreen.so
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_audiodevice.so
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_kdeconnect.so
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_wifi.so
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_bigscreen_settings.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name
