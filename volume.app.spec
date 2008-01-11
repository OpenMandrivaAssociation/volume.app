%define version 1.1
%define release %mkrel 3
%define name volume.app

Summary:  Simple volume control for AfterStep / BlackBox / WindowMaker
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://www.iskunk.org/soft/volume.app/
Requires:	xpm
BuildRequires:	X11-devel, xpm-devel
Prefix:		/usr/X11R6
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Volume.app is intended to be an extremely simple, efficient, and
attractive interface to a system's sound mixer. It differs from most other
dockapp mixer programs in that it does not require minute control of the
mouse to perform simple volume adjustments. It also lacks the ability to
monitor or control more than one mixer source at a time.

%prep

%setup -n %{name}-%{version}

%build
%make
     
%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}
tar xOjf %SOURCE1 %{name}-16x16.png > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-32x32.png > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-48x48.png > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{prefix}/bin/
install -m 755 %{name} $RPM_BUILD_ROOT%{prefix}/bin/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{prefix}/bin/%{name} -b
Icon=%{name}
Categories=Audio;
Name=Volume knob
Comment=Main Volume control dockapp
EOF


%clean
[ -z $RPM_BUILD_ROOT ] || {
    rm -rf $RPM_BUILD_ROOT
}


%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc ChangeLog AUTHORS INSTALL COPYING README TODO 
%{prefix}/bin/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

