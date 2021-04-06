# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}

%global gem_name smart_proxy_container_gateway
%global plugin_name container_gateway
%global gem_require_name %{gem_name}
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.2
Release: 2%{?dist}
Summary: Pulp 3 container registry support for Foreman/Katello Smart-Proxy
Group: Development/Languages
License: GPLv3
URL: http://github.com/ianballou/smart_proxy_container_gateway
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Autoreq: 0

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby < 3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(sequel)
Requires: %{?scl_prefix}rubygem(sqlite3)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5
BuildRequires: %{?scl_prefix_ruby}ruby < 3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Pulp 3 container registry support for Foreman/Katello Smart-Proxy.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bundler.d
%{gem_libdir}
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-2
- Rebuild plugins for Ruby 2.7

* Tue Feb 02 2021 ianballou <ianballou67@gmail.com> 1.0.2-1
- Update to 1.0.2

* Wed Jan 27 2021 ianballou <ianballou67@gmail.com> 1.0.1-1
- Update to 1.0.1

* Fri Jan 22 2021 ianballou <ianballou67@gmail.com> 1.0.0-1
- Add rubygem-smart_proxy_container_gateway generated by gem2rpm using the scl template

