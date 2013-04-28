Summary:	Tool to add extra metadata to rpm-md repositories
Name:		enhancerepo
Version:	0.4.3
Release:	0.2
License:	GPL v2+
Group:		Applications/System
Source0:	https://github.com/openSUSE/enhancerepo/tarball/master?/%{name}-%{version}.tgz
# Source0-md5:	c3a67eba426ee0f3ce21705d508fb32b
URL:		http://en.opensuse.org/openSUSE:Enhancerepo
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-activesupport >= 2.3
Requires:	ruby-builder
Requires:	ruby-ftools
Requires:	ruby-log4r >= 1.0.5
Requires:	ruby-nokogiri >= 1.4
Requires:	ruby-rpm
Requires:	ruby-rubygems >= 1.3.6
Requires:	ruby-trollop >= 1.0.5
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
%setup -qc
mv openSUSE-enhancerepo-0e25f21/* .

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
%doc README.rdoc TODO CHANGELOG.rdoc
%attr(755,root,root) %{_bindir}/enhancerepo
%{ruby_vendorlibdir}/enhance_repo.rb
%{ruby_vendorlibdir}/enhance_repo
%{ruby_vendorlibdir}/tempdir.rb
%{ruby_vendorlibdir}/tempdir
