# template: default
%global gem_name rack-test

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: Simple testing API built on Rack
License: MIT
URL: https://github.com/rack/rack-test
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0
BuildRequires: ruby >= 2.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md

%changelog
* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.0.2-1
- Update to 2.0.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-5
- Rebuild against rh-ruby27

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.0-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.0-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.1.0-2
- Bump for moving over to foreman-packaging

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-1
- Initial package