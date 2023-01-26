%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global commit 6a96698f42475975375b027b4d3bf5d8511b4a8f
%global gem_name jgrep

Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.3.3
Release:        11%{?dist}
Summary:        Query JSON structure with a matching language

Group:          Development/Tools
License:        ASL 2.0
URL:            http://jgrep.org/
Source0:        https://github.com/ploubser/JSON-Grep/archive/%{commit}/JSON-Grep-%{commit}.tar.gz
Patch0:         0001-Fix-test-run.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
BuildRequires:  %{?scl_prefix_ruby}rubygem(json)
Requires:       %{?scl_prefix_ruby}ruby(release) >= 1.8
Requires:       %{?scl_prefix_ruby}rubygems
Requires:       %{?scl_prefix_ruby}rubygem(json)
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
JGrep is  Ruby-based CLI tool and API for parsing and displaying JSON data
using a logical expression syntax. It allows you to search a list of JSON
documents and return specific documents or values based on logical truths.


%package doc
Summary:        Documentation for %{pkg_name}
Group:          Documentation
Requires:       %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
Documentation for %{pkg_name}


%prep
%setup -qn JSON-Grep-%{commit}
%patch0 -p1

%{?scl:scl enable %{scl} - <<EOF}
gem build %{gem_name}.gemspec
%gem_install -n %{gem_name}-%{version}.gem
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}


%files
%{_bindir}/*
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/*.gemspec
%{gem_spec}
%doc COPYING README.markdown


%files doc
%{gem_docdir}


%changelog
* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.3.3-11
- Rebuild for Ruby 2.7

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.3-10
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.3.3-9
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.3.3-8
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.3.3-7
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.3.3-6
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 1.3.3-5
- Import from Fedora and SCLise (dcleal@redhat.com)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-3
- Disable tests on rhel

* Tue Apr 29 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-2
- Run tests (Lukas Bezdicka, #1092000)
- Fix issue with tests. (Guess adding the run was a good idea...)

* Mon Apr 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-1
- Initial packaging