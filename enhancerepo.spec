Summary:	Tool to add extra metadata to rpm-md repositories
Name:		enhancerepo
Version:	0.4.1
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	https://github.com/openSUSE/enhancerepo/archive/release-%{version}.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	8a61b704f7aaba7f142889b162111530
URL:		http://en.opensuse.org/openSUSE:Enhancerepo
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-rpm
Requires:	ruby-rubygems
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
enhancerepo is a tool to add extra metadata to rpm-md repositories. It
is supposedly to be run on top of a repository created with the
upstream createrepo.

It will add the extra data to extension files, and add them to the
repository index, doing all the dirty work of updating the index and
compressing the files.

Features:
- Signing of repositories
- Adding package eulas from files to susedata.xml
- Adding package keywords from files to susedata.xml
- Adding package disk usage information to susedata.xml
- Add expiration time, product compatibility, keywords to repository
  susenfo.xml (experimental)
- Add deltarpm information to the repository.
- Easily create patches

%prep
%setup -q -n %{name}-release-%{version}

%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGELOG.rdoc
%attr(755,root,root) %{_bindir}/enhancerepo
%{ruby_vendorlibdir}/enhance_repo.rb
%{ruby_vendorlibdir}/enhance_repo
%{ruby_vendorlibdir}/tempdir.rb
%{ruby_vendorlibdir}/tempdir
