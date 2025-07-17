# Spec file for Hysteria RPM package

%global goipath         github.com/apernet/hysteria

Name:           hysteria
# using --define "version <the_actual_version>"
Version:        0.0.0
Release:        1%{?dist}
Summary:        Hysteria is a feature-packed proxy & relay tool built for poor network conditions.

License:        MIT
URL:            https://%{goipath}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  git
BuildRequires:  make
BuildRequires:  python3

%description
Hysteria is a powerful, feature-packed proxy and relay tool designed to work
efficiently in adverse network environments. It's known for its high performance
and ability to bypass network restrictions.

%prep
%setup -q -n hysteria-app-v%{version}

git init

%build
# Using the build script provided in the source
HY_APP_VERSION=v%{version} python3 hyperbole.py build -r

%install
install -D -m 755 build/hysteria-v%{version}-linux-amd64 %{buildroot}%{_bindir}/hysteria

%files
%license LICENSE
%doc README.md
%{_bindir}/hysteria

%changelog
* Wed Jul 17 2024 Your Name <your.email@example.com> - 0.0.0-1
- Initial automated RPM build setup
