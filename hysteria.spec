
Name:           hysteria
# This version is a placeholder and will be updated by the workflow
Version:        0.0.0
Release:        1%{?dist}
Summary:        Hysteria is a feature-packed proxy & relay tool built for poor network conditions.

License:        MIT
URL:            https://%{goipath}
Source0:        %{name}-%{version}.tar.gz
Source1:        hysteria.service
Source2:        hysteria.yaml

BuildRequires:  golang
BuildRequires:  git
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  systemd

%global debug_package %{nil}

%description
Hysteria is a powerful, feature-packed proxy and relay tool designed to work
efficiently in adverse network environments. It's known for its high performance
and ability to bypass network restrictions.

%prep
%setup -q -n hysteria-app-v%{version}

git init
git config --global user.email "builder@example.com"
git config --global user.name "RPM Builder"
git add .
git commit --allow-empty -m "Initial commit for RPM build"
git tag "app/v%{version}"

%build
# Using the build script provided in the source
python3 hyperbole.py build -r

%install
# Install the binary
install -D -m 755 build/hysteria-linux-amd64 %{buildroot}%{_bindir}/hysteria

# Install systemd service file
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/hysteria.service

# Install default config file
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/hysteria.yaml

%post
%systemd_post hysteria.service

%preun
%systemd_preun hysteria.service

%postun
%systemd_postun_with_restart hysteria.service

%files
%license LICENSE.md
%doc README.md
%{_bindir}/hysteria
%{_unitdir}/hysteria.service
%config(noreplace) %{_sysconfdir}/hysteria.yaml

%changelog
* Wed Jul 17 2024 Your Name <your.email@example.com> - 0.0.0-1
- Initial automated RPM build setup
- Added systemd service
