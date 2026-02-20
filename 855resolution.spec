Summary:	Change the resolution of an available vbios mode for the 855/865/915 Intel graphic chipset
Summary(pl.UTF-8):	Zmiana rozdzielczości dostępnych trybów vbios dla chipsetów Intel 855/865/915
Name:		855resolution
Version:	0.4
Release:	2
License:	Public Domain
Group:		Applications/System
Source0:	http://perso.wanadoo.fr/apoirier/%{name}-%{version}.tgz
# Source0-md5:	12237e534def7dd3579a3e8b0a4b9351
Source1:	%{name}.sysconfig
Source2:	%{name}.init
URL:		http://perso.wanadoo.fr/apoirier/
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
855resolution is a software to change the resolution of an available
vbios mode for the 855/865/915 Intel graphic chipset. It was
originally coded it to get the 1400x1050 resolution on Dell 510.

Later it was tested with success on the following laptops:
- Acer Travelmate 291lmi
- Acer TravelMate 661LCi
- Acer Travelmate 662
- Asus M3N
- Dell Inspiron 500m
- Dell Inspiron 510m
- Dell Inspiron 700m
- Fujitsu LifeBook P5010D
- Fujitsu E4010

It patches only the RAM version of the video BIOS so the new
resolution is loose each time you reboot. If you want to set the
resolution each time you reboot and before to launch X, use
appropriate init script file of your Linux version.

%description -l pl.UTF-8
855resolution to program do zmiany rozdzielczości dostępnych trybów
vbios dla chipsetów graficznych Intel 855/865/915. Pierwotnie był
napisany w celu uzyskania rozdzielczości 1400x1050 na Dellu 510.

Później został pozytywnie przetestowany na następujących laptopach:
- Acer Travelmate 291lmi
- Acer TravelMate 661LCi
- Acer Travelmate 662
- Asus M3N
- Dell Inspiron 500m
- Dell Inspiron 510m
- Dell Inspiron 700m
- Fujitsu LifeBook P5010D
- Fujitsu E4010

Program modyfikuje tylko wersję w RAM Video BIOS-u, więc nowa
rozdzielczość jest tracona po każdym reboocie. Aby ustawiać
rozdzielczość po każdym uruchomieniem komputera, a przed uruchomieniem
X, należy użyć odpowiedniego skryptu inicjalizującego.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,sysconfig}}

install 855resolution $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add 855resolution

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del 855resolution
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) %{_sbindir}/*
