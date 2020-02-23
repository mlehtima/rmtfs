Name:          rmtfs
Version:       1.0
Release:       1
Summary:       Qualcomm Remote Filesystem Service Implementation
URL:           https://github.com/andersson/rmtfs
Source0:       %{name}-%{version}.tar.gz
License:       BSD-3-Clause
BuildRequires: pkgconfig(udev)
BuildRequires: qrtr-devel

%description
Qualcomm Remote Filesystem Service Implementation

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%make_build

%install
make prefix=%{_prefix} libdir=%{_libdir} install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_unitdir}/multi-user.target.wants
ln -s ../%{name}.service %{buildroot}/%{_unitdir}/multi-user.target.wants/%{name}.service

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_unitdir}/multi-user.target.wants/%{name}.service
%{_unitdir}/%{name}.service
