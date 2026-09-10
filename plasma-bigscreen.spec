%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A privacy-respecting, open source and secure TV ecosystem
Name:		plasma-bigscreen
Version:	6.7.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://plasma-bigscreen.org/
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(KF6BluezQt)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Screen)
BuildRequires:	cmake(Plasma)
BuildRequires:	%mklibname Plasma -d
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(PlasmaActivitiesStats)
BuildRequires:	cmake(LibKWorkspace)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(Wayland)
BuildRequires:	pkgconfig(sdl3)

BuildSystem:	cmake
BuildOption:	-DBUILD_TESTING:BOOL=OFF
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

Requires:	plasma-workspace
Requires:	plasma-nano
Requires:	qml(org.kde.plasma.core)

%description
A 10-foot user interface for TVs and set-top boxes, built on Plasma.

%files -f %{name}.lang
%{_bindir}/plasma-bigscreen*
%{_datadir}/wayland-sessions/plasma-bigscreen*
%{_datadir}/applications/org.kde.plasma.bigscreen*
%{_datadir}/applications/org.kde.bigscreen*
%{_datadir}/metainfo/org.kde.plasma.bigscreen.metainfo.xml
%{_datadir}/plasma/shells/org.kde.plasma.bigscreen*
%{_datadir}/plasma/plasmoids/org.kde.*bigscreen*
%{_datadir}/plasma/plasmoids/org.kde.biglauncher*
%{_datadir}/plasma/look-and-feel/org.kde.plasma.bigscreen*
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen*
%{_datadir}/sounds/plasma-bigscreen
%{_datadir}/dbus-1/interfaces/org.kde.biglauncher.xml
%{_libdir}/udev/rules.d/40-uinput.rules
