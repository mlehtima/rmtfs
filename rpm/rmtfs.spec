Name:          rmtfs
Version:       0.2
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
%autosetup -n %{name}-%{version}/rmtfs

%build
make %{?_smp_mflags}

%install
make prefix=/usr install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_libdir}/systemd/system/multi-user.target.wants
ln -s ../rmtfs.service %{buildroot}/%{_libdir}/systemd/system/multi-user.target.wants/rmtfs.service

%clean
make clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/rmtfs
%{_libdir}/systemd/system/multi-user.target.wants/rmtfs.service
%{_libdir}/systemd/system/rmtfs.service
