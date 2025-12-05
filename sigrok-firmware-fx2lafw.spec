%define sourcedate 20251203
%define gitcommit 0f2d324

# NOTE To update this package run package-source.sh in order to create a new source
# NOTE tarball from the latest upstream git master branch.
# NOTE The script will adjust sourcedate & gitcommit defines to match created tarball.
# NOTE You may have to reload this file to see the changed values.

Name:		sigrok-firmware-fx2lafw
Version:	0.1.7+git%{sourcedate}.%{gitcommit}
Release:	1
Summary:	Open Source Firmware for Logic Analyzers based on the Cypress EZ-USB FX2(LP) Chip
URL:		http://www.sigrok.org
License:	GPL
Group:		Hardware/Other
# Using source from git as it is up to date & has bugfixes vs release.
Source0:	sigrok-firmware-fx2lafw-%{sourcedate}-%{gitcommit}.tar.zst
# Original upstream source
#Source0:	https://sigrok.org/download/source/%%{name}/%%{name}-%%{version}.tar.gz
# Alternative GH source
#Source0:	https://github.com/sigrokproject/sigrok-firmware-fx2lafw/archive/%%{version}/%%{name}-%%{version}.tar.gz

BuildRequires:	autoconf automake slibtool
BuildRequires:	make
BuildRequires:	sdcc
BuildArch:	noarch

%description
fx2lafw is an open-source firmware for Cypress FX2 chips which makes them usable as simple logic analyzer and/or oscilloscope hardware.

%prep
%autosetup -n %{name}-%{sourcedate}-%{gitcommit} -p1

%build
sh autogen.sh
%configure
make

%install
%make_install

%files
%doc README NEWS
%license COPYING COPYING.LESSER
%{_datadir}/sigrok-firmware/fx2lafw-*.fw
